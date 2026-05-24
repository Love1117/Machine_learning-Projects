from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path
import os
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

vector = joblib.load(MODEL_DIR / "vector.joblib")
tfidf = joblib.load(MODEL_DIR / "tfidf.joblib")
movies = joblib.load(MODEL_DIR / "movies.joblib")


app = FastAPI()

class MovieRequest(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}


@app.post("/recommend")
def get_movie_recommendations(request: MovieRequest):
    try:
        title = request.title

        idx = movies[movies["Title"].str.lower() == title.lower()].index[0]
        sim_scores = sorted(list(enumerate(cosine_similarity(vector[idx], vector).flatten())), reverse=True,  key= lambda item: item[1])

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
