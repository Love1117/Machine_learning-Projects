from fastapi import APIRouter
from app.schemas.music_schema import MusicRequest
from app.services.music_service import recommend_music




router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.get("/songs")
def get_songs():
    song_list = songs["track_name"].tolist()
    return {
        "songs": song_list
    }

@router.post("/recommend")
def get_song_recommendations(request: MusicRequest):
    return recommend_music(request.track_name)