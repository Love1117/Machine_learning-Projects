from pydantic import BaseModel

class MusicRequest(BaseModel):
    brand: str
