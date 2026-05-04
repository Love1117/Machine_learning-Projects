from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import PredictionRequest
from app.services.predict_service import predict_image
from app.database.session import get_db

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CIFAR-10 images classification API is running"}

@router.get("/model_check")
def model_check():
    return {"status": "ok"}

@router.post("/predict")
async def predict_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    return await predict_image(data:PredictionRequest, file, db)
