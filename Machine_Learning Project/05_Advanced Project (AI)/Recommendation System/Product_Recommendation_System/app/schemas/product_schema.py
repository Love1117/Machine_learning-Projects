from pydantic import BaseModel

class MobileRequest(BaseModel):
    category: str
