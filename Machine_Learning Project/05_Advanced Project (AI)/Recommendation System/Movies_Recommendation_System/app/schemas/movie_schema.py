from pydantic import BaseModel

class MovieRequest(BaseModel):
    title: str
