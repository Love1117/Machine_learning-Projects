from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  age: int = Field(..., example=19, description="Age")
  sex: Literal["Male","Female"]
  bmi: float = Field(..., example=27.900, description="Bmi")
  children: int = Field(..., example=0, description="Children")
  smoker: Literal["Yes","No"]
  region: int = Field(..., example=3, description="Region")
  charges: float = Field(..., example=16884.92400, description="Charges")
