from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path


# Model directory
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

# Load models
phone_data = joblib.load(MODEL_DIR, "phone_data.joblib")
vector = joblib.load(MODEL_DIR, "vector.joblib")



def strikethrough_text(text):
    return ''.join([char + '\u0336' for char in str(text)])

def rating_to_stars(rating, max_stars=5):
    full_stars = int(rating)
    half_star = math.ceil(rating) > full_stars and (rating - full_stars >= 0.5)
    empty_stars = max_stars - full_stars - (1 if half_star else 0)

    stars_string = '⭐' * full_stars
    if half_star:
        stars_string += '⭐️' # half-star emoji, or use a different one if preferred
    stars_string += '☆' * empty_stars
    return stars_string



# Request schema
class MobileRequest(BaseModel):
    brand: str



# Initialize FastAPI
app = FastAPI(
    title="Mobile Recommendation API",
    version="1.0"
)



@app.get("/")
def home():
    return {"message": "Mobile Recommendation API is running"}



# Recommendation endpoint
@app.post("/recommend")
def recommend_mobile(request: MobileRequest):
  try:
    requested_brand = request.brand

    idx = phone_data[phone_data["brand"].str.lower() == requested_brand.lower()].index

    if idx.empty:
        raise HTTPException(status_code=404,
            detail=f"brands '{requested_brand}' not found")
            
    # Use the first matching phone's vector as the reference for similarity
    # Reshape to (1, -1) because cosine_similarity expects 2D arrays
    brand_reference_vector = vector[idx[0]].reshape(1, -1)

    # Calculate cosine similarity between the reference vector and all phone vectors
    sim_scores_raw = cosine_similarity(brand_reference_vector, vector).flatten()

    # Pair each similarity score with its original index and sort in descending order
    sim_scores = sorted(list(enumerate(sim_scores_raw)),
                        reverse=True,  key= lambda item: item[1])

    recommendations = []

    # Get top 10 recommendations, skipping the first one (which is the input phone itself)
    for i in sim_scores[1:11]:
      recommended_phone = phone_data.iloc[i[0]]
      market_price_formatted = strikethrough_text(recommended_phone['market_price'])
      star_rating = rating_to_stars(recommended_phone['rating'])

      recommendations.append({
                "image_url": recommended_phone['image_url'],
                "product_name": recommended_phone['name'],
                # Include both star emojis and the numerical rating with 'out of 5 stars;
                "rating": f"{star_rating} {recommended_phone['rating']} ({recommended_phone['ratings_reviews']})Comments",
                "sale_price": f"{recommended_phone['discount']} ${recommended_phone['Sale_Price']}",
                "market_price": f"${market_price_formatted}"
            })
    return recommendations
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
