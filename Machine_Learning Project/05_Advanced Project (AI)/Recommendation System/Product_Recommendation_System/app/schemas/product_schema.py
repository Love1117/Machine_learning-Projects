from pydantic import BaseModel

class ProductRequest(BaseModel):
    category: str
