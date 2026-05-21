from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os


output_dir = "/content/drive/My Drive/Models/Advanced Project/Recommendation System/"

# Load the vector and similarity matrix
vector = joblib.load(os.path.join(output_dir, "Vector.joblib"))
similarity = joblib.load(os.path.join(output_dir, "similarity.joblib"))
movies = joblib.load(os.path.join(output_dir, "movies.joblib"))

app = FastAPI()

class MovieRequest(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}


def get_recommendations(title):
  idx = movies[movies["Title"]== title].index[0]
  sim_scores = sorted(list(enumerate(similarity[idx])), reverse=True,  key= lambda vector: vector[1])
  for i in sim_scores[1:11]:
    print(movies.iloc[i[0]].Title)

@app.post("/recommend")
def get_movie_recommendations(request: MovieRequest):
    try:
        title = request.title

        
        idx = movies[movies["Title"] == request.title].index[0]
        sim_scores = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

        # Get the top 10 similar movies (excluding the movie itself)
        recommendations = []
        for i in sim_scores[1:11]:
            movie_data = movies.iloc[i[0]]
            recommendations.append({"title": movie_data.Title, "poster": movie_data.Poster})

        return {"movie": title, "recommendations": recommendations}
    except IndexError:
        return {"error": f"Movie '{request.title}' not found in the database."}, 404
    except Exception as e:
        return {"error": str(e)}, 500
