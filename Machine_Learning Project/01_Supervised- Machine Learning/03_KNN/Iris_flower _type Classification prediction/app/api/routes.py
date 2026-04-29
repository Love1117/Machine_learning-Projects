from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db


router = APIRouter()


@router.get("/model_check")
def model_check():
    return {"status": "ok"}

@router.get("/model_info")
def info():
  return {"Project_name": "Iris Flower type prediction based on petal, sepal (length and weight)",
          "Features": ["sepal length (cm)",
                        "sepal width (cm)",
                        "petal length (cm)",
                        "petal width (cm)",
                        "target"],
           "Version": "v1.0.0"}

@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return prediction(data, db)
