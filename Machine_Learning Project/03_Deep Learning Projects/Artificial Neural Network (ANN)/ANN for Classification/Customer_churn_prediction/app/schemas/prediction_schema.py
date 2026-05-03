from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  gender: Literal["Male","Female"]
  SeniorCitizen: Literal["Yes","No"]
  Partner: Literal["Yes","No"]
  Dependents: Literal["Yes","No"]
  tenure: int= Field(..., example=1, description="What is your monthly charges")
  PhoneService: Literal["Yes","No"]
  MultipleLines: Literal["Yes","No"]
  OnlineSecurity: Literal["Yes","No"]
  OnlineBackup: Literal["Yes","No"]
  DeviceProtection: Literal["Yes","No"]
  TechSupport: Literal["Yes","No"]
  StreamingTV: Literal["Yes","No"]
  StreamingMovies: Literal["Yes","No"]
  PaperlessBilling: Literal["Yes","No"]
  MonthlyCharges: float= Field(..., example=29.85, description="What's your monthly charges")
  TotalCharges: float= Field(..., example=29.85, description="What's your total charges")
  PaymentMethod_status: str= Field(..., example="Credit card (automatic)", description="Payment method")
  Contract_status: str= Field(..., example="One year", description="Years of contract")
  InternetService_status: str= Field(..., example="DSL", description="Internet Service")
