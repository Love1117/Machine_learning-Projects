from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  Home_ID: int= Field(..., example=94, description="Home_ID")
  Outdoor_Temperature_C: float= Field(..., example=-1.0, description="Outdoor_Temperature_(°C)")
  Household_Size: float= Field(..., example=2, description="Household size")
  Year: int= Field(..., example=2023, description="Year")
  Month: int= Field(..., example=12, description="Month")
  Day: int= Field(..., example=2, description="Month")
  Days_Of_The_Week: int= Field(..., example= 5, description="Days_Of_The_Week")
  Hour: float= Field(..., example=21, description="Hour")
  Weekend: Literal["Yes","No"]
  Appliance_Type_status: str= Field(..., example="Dishwasher", description="Appliance_Type")
  Season_status: str= Field(..., example="Spring", description="Season")
