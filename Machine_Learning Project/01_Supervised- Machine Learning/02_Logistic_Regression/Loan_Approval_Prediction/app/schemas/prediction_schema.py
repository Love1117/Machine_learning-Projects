from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  Age: float= Field(..., example=25, description="Fill in the space")
  Gender: Literal["Male","Female"]
  Education: Literal["High School", "Associate", "Bachelor", "Master", "Doctorate"]
  Income: float= Field(..., example=66135.0, description="Fill in the space")
  Employment_experience:int= Field(..., example=3, description="Fill in the space")
  Home_ownership: str
  Loan_amount: float= Field(..., example=35000.0, description="Fill in the space")
  Loan_intent: str
  Loan_interest_rate: float= Field(..., example=16.02, description="Fill in the space")
  Loan_percent_income: float= Field(..., example=0.53, description="Fill in the space")
  Credit_history_length: float= Field(..., example=3.0, description="Fill in the space")
  Credit_score: int= Field(..., example=617, description="Fill in the space")
  Previous_loan_defaults_on_file: Literal["Yes","No"]
