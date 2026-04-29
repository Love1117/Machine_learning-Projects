from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db
from app.services.model_loader import AddressAndCity_Encoder, State_Encoder, County_Encoder


router = APIRouter()

@router.get("/options")
def get_options():
    return {
        "Address_And_City": list(AddressAndCity_Encoder.keys()),
        "State": list(State_Encoder.keys()),
        "County": list(County_Encoder.keys())
    }

@router.get("/model_check")
def model_check():
    return {"status": "ok"}

@router.get("/Model/{used_model}")
def Model_Info(used_model: str="Linear_Regression"):
  return {"model":{used_model},
          "Features":["Bedrooms",
                      "Bathrooms",
                      "Living_Space",
                      "Median_Household_Income",
                      "Zip_Code",
                      "Latitude",
                      "Longitude",
                      "Address_And_City",
                      "State",
                      "County",
                      "Price"],
          "Version":"v1.0.0.0"}

@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return prediction(data, db)
