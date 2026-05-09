from app.schemas.prediction_schema import ChatRequest


router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.post("/chat", summary="Generate text using Llama 3.2")
def generate_chat_response(request: ChatRequest):
    return prediction(request)
