import pandas as pd
from fastapi import HTTPException
from app.services.preprocessing import get_song_album_cover_url
from sklearn.metrics.pairwise import cosine_similarity
from app.services.model_loader import songs, matrix



def recommend_music(request: MusicRequest):
    try:
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
            song.artist_name),

            "music_title": song.track_name,

            "artist_name": song.artist_name})

        return {
            "requested_song": requested_track,
            "recommendations": recommendations}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))