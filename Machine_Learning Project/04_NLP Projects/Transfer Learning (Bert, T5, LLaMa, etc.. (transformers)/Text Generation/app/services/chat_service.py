import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from typing import Dict, Any
from app.core.config import HF_TOKEN



client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

def generate_chat_response(request: ChatRequest) -> Dict[str, Any]:
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct:novita",
            messages=[{"role": "user", "content": request.text}]
        )
        return {"response": completion.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Llama model error: {e}")
