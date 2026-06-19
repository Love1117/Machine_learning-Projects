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
  Profession_status: Literal["Artist", "Doctor", "Engineer", "Entertainment", "Executive", "Healthcare", "Homemaker", "Lawyer", "Marketing"]
  Variable_status: Literal["Cat_1", "Cat_2", "Cat_3", "Cat_4", "Cat_5", "Cat_6", "Cat_7"]
