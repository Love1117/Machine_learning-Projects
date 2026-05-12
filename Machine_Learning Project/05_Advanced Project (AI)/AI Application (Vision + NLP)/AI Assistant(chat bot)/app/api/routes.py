from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional

router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/chat")
def chat_with_model(
    question: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    """
    Generates a chat/image response using the gemma-3-27b-it model.
    """
    return await predict_chat(question, image)
