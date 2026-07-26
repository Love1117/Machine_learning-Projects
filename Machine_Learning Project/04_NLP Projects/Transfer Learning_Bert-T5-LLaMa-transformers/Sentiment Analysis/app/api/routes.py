from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import TextRequest
from app.services.predict_service import prediction
from app.database.session import get_db



router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/predict-roberta")
def predict_roberta_sentiment(request: TextRequest, db: Session = Depends(get_db)):
     """
  Analyzes the sentiment of the provided text using the VADER model.
  Returns polarity scores (negative, neutral, positive, compound).
  """
    return prediction(request, db)
