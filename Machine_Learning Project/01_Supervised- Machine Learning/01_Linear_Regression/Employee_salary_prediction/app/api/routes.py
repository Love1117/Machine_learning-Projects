from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db
from app.services.model_loader import Country_freq, Race_freq, Job_title_encoder


router = APIRouter()

@router.get("/options")
def get_options():
    return {
        "Country": list(Country_freq.keys()),
        "Race": list(Race_freq.keys()),
        "Job_title": list(Job_title_encoder.keys())
    }

@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return predict_salary(data, db)
