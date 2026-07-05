from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Assistant(chat bot) API",
    description="API for meta-llama 3.3 Chatbot/AI Assistant",
    version="1.0.0")


@app.get("/")
def home():
    return {"message": "FastAPI is running"}


app.include_router(router)
