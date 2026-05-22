import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import movies, similarity


def recommendation(request):
    try:
        title = request.title

        
        idx = movies[movies["Title"] == request.title].index[0]
        sim_scores = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])

        # Get the top 10 similar movies (excluding the movie itself)
        recommendations = []
        for i in sim_scores[1:11]:
            movie_data = movies.iloc[i[0]]
            recommendations.append({"title": movie_data.Title, "poster": movie_data.Poster})

        return {"movie": title, 
                "recommendations": recommendations}
    except IndexError:
        return {"error": f"Movie '{request.title}' not found in the database."}, 404
    except Exception as e:
        return {"error": str(e)}, 500
