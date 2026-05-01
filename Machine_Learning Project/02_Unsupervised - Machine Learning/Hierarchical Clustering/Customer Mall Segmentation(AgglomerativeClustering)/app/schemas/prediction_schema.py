from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  Gender: Literal["Male", "Female"]
  Age: int= Field(..., example=44, description="input your age")
  Annual_Income_k: float= Field(..., alias="Annual_Income_(k$)", example=73, description="what is your annual income")
  Spending_Score_1_100: float= Field(..., alias="Spending_Score(1-100)", example=7, description="what is your spending score")
