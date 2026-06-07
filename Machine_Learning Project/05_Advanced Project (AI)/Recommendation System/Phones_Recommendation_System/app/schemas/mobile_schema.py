from pydantic import BaseModel

class MobileRequest(BaseModel):
    brand: str
