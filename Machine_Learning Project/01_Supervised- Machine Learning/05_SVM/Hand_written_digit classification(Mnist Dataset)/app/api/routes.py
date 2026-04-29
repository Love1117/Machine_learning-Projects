from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session

from app.services.predict_service import predict_digit
from app.database.session import get_db

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Digit Image Recognition API is running"}

@router.get("/model_check")
def model_check():
    return {"status": "ok"}

@router.post("/predict")
async def predict_digit_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    return await predict_digit(file, db)
