from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import ChatRequest
from app.services.predict_service import prediction
from app.database.session import get_db


router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/chat", summary="Generate text using Llama 3.2")
def generate_chat_response(request: ChatRequest, db: Session = Depends(get_db)):
    return prediction(request, db)
