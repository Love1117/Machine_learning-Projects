from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import predict_price
from app.database.session import get_db

router = APIRouter()

@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return predict_price(data, db)
