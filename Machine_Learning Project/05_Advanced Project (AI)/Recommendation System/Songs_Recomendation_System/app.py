from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import os
from sklearn.metrics.pairwise import cosine_similarity
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI(
    title="Music Recommendation API",
    version="1.0"
)

# Model directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Load models
matrix = joblib.load(os.path.join(MODEL_DIR, "matrix.joblib"))
songs = joblib.load(os.path.join(MODEL_DIR, "songs.joblib"))

# Spotify credentials
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Spotify authentication
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Request schema
class MusicRequest(BaseModel):
    track_name: str

# Root route
@app.get("/")
def home():
    return {"message": "Music Recommendation API is running"}

# Get album image
def get_song_album_cover_url(song_name, artist_name):
    try:
        query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=query, type="track", limit=1)
        tracks = results.get("tracks", {}).get("items", [])

        if tracks:
            images = tracks[0]["album"].get("images", [])
            if images:
                return images[0]["url"]

        return "https://i.imgur.com/8zQZQ9G.png"

    except Exception:
        return "https://i.imgur.com/8zQZQ9G.png"

# Recommendation endpoint
@app.post("/recommend")
def recommend_music(request: MusicRequest):
    requested_track = request.track_name
    matching_indices = songs[songs["track_name"].str.lower() == requested_track.lower()].index

    if matching_indices.empty:
        raise HTTPException(status_code=404,
            detail=f"Song '{requested_track}' not found")

    idx = matching_indices[0]

    similarity_scores = cosine_similarity(matrix[idx],matrix).flatten()

    sim_scores = sorted(
        list(enumerate(similarity_scores)),
        key=lambda x: x[1],
        reverse=True)

    recommendations = []

    for i in sim_scores[1:11]:
        song = songs.iloc[i[0]]

        recommendations.append({
    "poster": get_song_album_cover_url(
        song.track_name,
        song.artist_name
    ),

    "music_title": song.track_name,

    "artist_name": song.artist_name})

    return {
        "requested_song": requested_track,
        "recommendations": recommendations
    }
