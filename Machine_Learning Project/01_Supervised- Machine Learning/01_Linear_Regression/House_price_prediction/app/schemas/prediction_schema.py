from pydantic import BaseModel, Field
from typing import Literal

class Base(BaseModel):
  Bedrooms: int= Field(..., example=2, description="fill in numbers of bedroom")
  Bathrooms: int= Field(..., example=3, description="fill in numbers of bathroom")
  Living_Space: int= Field(..., example=1538, description="fill in the size of Living Space")
  Median_Household_Income: float= Field(..., example=370046.00, description="Median_Household_Income")
  Zip_Code: float= Field(..., example=10017, description="Zip Code")
  Latitude: float= Field(..., example=40.72, description="Latitude")
  Longitude: float= Field(..., example=-74.00, description="Longitude")
  Address_And_City: str
  State: str
  County: str
