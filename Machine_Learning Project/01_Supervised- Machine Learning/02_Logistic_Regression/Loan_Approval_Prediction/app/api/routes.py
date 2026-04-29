from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db
from app.services.model_loader import Loan_intent_freq, Home_ownership_freq


router = APIRouter()

@router.get("/options")
def get_options():
    return {
        "Loan_intent": list(Loan_intent_freq.keys()),
        "Home_ownership": list(Home_ownership_freq.keys())}

@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return prediction(data, db)
