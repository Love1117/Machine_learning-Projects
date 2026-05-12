from fastapi import FastAPI
from app.api.routes import router



app = FastAPI(
    title="AI Assistant(chat bot) API",
    description="API for google/gemma-3-27b-it Chatbot/AI Assistant",
    version="1.0.0")
    
app.include_router(router)
