from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
    car_ModelAndYear: str
    car_name: str
    year: int = Field(..., example=2018)
    km_driven: float
    transmission: Literal["Automatic", "Manual"]
    mileage: float
    engine: float
    max_power: float
    seats: float
    fuel: Literal["Diesel","Petrol","LPG","CNG"]
    owner: Literal[
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
    seller_type: Literal["Individual", "Dealer", "Trustmark Dealer"]
