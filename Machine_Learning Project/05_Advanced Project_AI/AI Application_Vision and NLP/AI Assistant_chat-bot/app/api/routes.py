from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from app.services.chat_service import predict_chat
from fastapi import APIRouter


router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/chat")
async def chat_with_model(
    question: str = Form(""),
    image: Optional[UploadFile] = File(None),
    audio: Optional[UploadFile] = File(None)
):
    """
    Generates a chat/image/audio response using meta-llama 3.3 model.
    """
    return await predict_chat(
        question=question,
        image=image,
        audio=audio)
