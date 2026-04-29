from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db
from app.services.model_loader import car_model_encoder, car_name_encoder


router = APIRouter()

@router.get("/options")
def get_options():
    return {
        "car_model_and_year": list(car_model_encoder.keys()),
        "car_names": list(car_name_encoder.keys())
    }



@router.get("/model_check")
def model_check():
    return {"status": "ok"}

@route.get("/model_info")
def model_info():
  return {"model_type":"Linear_Regresion",
          "Features":["car_model",
                      "year",
                      "car_name",
                      "km_driven",
                      "transmission",
                      "millage",
                      "engine",
                      "max_power",
                      "seats",
                      "fuel",
                      "seller_type",
                      "owner",
                      "selling_price"],
          "Version": "v1.0.0.0"}

@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return prediction(data, db)
