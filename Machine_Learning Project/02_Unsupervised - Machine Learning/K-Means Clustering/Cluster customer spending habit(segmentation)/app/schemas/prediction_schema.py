from pydantic import BaseModel, Field
from typing import Literal


class PredictionRequest(BaseModel):
  Gender: Literal["Male", "Female"]
  Ever_Married: Literal["Yes", "No"]
  Age: int= Field(..., example=36, description="input your age")
  Graduated: Literal["Yes", "No"]
  Work_Experience: float= Field(..., example=8.0, description="work_experience")
  Spending_Score: int= Field(..., example=3, description="spending score")
  Family_Size: float= Field(..., example=3.0, description="work_experience")
  Profession_status: str= Field(..., example="Doctor", description="profession")
  Variable_status: str= Field(..., example="cat_2", description="input variable")
