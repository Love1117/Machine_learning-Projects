from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import prediction
from app.database.session import get_db



router = APIRouter()


@router.post("/predict")
def predict(data: PredictionRequest, db: Session = Depends(get_db)):
    return prediction(data, db)
