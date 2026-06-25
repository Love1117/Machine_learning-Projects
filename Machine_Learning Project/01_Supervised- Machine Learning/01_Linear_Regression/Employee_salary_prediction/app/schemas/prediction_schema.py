from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  Age: int
  Gender: Literal["Male","Female"]
  Education_Level: Literal["High School", "Bachelor's", "Master's", "PhD"]
  Years_of_Experience: float
  Country: str
  Race: str
  Senior: Literal["Yes","No"]
  Job_title: str
