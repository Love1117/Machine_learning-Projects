from pydantic import BaseModel

class MusicRequest(BaseModel):
    track_name: str