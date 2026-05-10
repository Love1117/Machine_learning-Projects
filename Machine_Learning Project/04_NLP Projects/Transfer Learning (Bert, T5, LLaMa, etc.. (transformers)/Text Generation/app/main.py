from fastapi import FastAPI
from app.api.routes import router



app = FastAPI(
    title="LLaMA 3.2 Text Generation API",
    description="API for Meta LLaMA 3.2 Chatbot",
    version="1.0.0")
    
app.include_router(router)
