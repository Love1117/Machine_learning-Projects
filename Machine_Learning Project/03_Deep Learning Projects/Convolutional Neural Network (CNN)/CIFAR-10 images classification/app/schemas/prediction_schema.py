from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  filename: str
  predicted_class_name: str
  confidence: float
