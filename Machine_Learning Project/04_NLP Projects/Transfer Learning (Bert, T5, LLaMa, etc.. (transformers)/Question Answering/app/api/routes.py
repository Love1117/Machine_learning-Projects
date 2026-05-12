from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import Question
from app.services.predict_service import prediction
from app.database.session import get_db

router = APIRouter()

@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/predict_answer")
def def predict_answer(question_data: Question, db: Session = Depends(get_db)):
    return prediction(question_data, db)
