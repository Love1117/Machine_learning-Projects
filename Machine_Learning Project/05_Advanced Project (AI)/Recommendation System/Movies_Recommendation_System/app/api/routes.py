from app.schemas.movie_schema import MovieRequest
from app.services.movie_service import recommendation




router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.get("/movies")
def get_movies():
    movie_list = movies["Title"].tolist()
    return {
        "movies": movie_list
    }

@router.post("/recommend")
def get_movie_recommendations(request: MovieRequest):
    return recommendation(request.title)
