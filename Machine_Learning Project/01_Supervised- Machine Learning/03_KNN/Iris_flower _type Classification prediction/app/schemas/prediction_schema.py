from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  sepal_length: float
  sepal_width: float
  petal_length: float
  petal_width: float
