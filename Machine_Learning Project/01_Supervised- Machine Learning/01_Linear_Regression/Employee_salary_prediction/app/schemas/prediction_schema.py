from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  Age: float
  Gender: Literal["Male","Female"]
  Education_Level: int
  Years_of_Experience: float
  Country: str
  Race: str
  Senior: int
  Job_title: str
