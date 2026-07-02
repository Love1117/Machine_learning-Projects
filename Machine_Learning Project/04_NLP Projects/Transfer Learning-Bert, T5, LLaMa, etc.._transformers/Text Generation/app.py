import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv
import uvicorn

load_dotenv()


HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found")


client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)


app = FastAPI(
    title="LLaMA 3.2 Text Generation API",
    description="API for Meta LLaMA 3.2 Chatbot",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    text: str


@app.post("/chat", summary="Generate text using Llama 3.2")
async def generate_chat_response(request: ChatRequest) -> Dict[str, Any]:
    """
    Generates a chat response using the Meta LLaMA 3.2 model.
    """
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct:novita",
            messages=[{"role": "user", "content": request.text}]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Llama model error: {e}")
