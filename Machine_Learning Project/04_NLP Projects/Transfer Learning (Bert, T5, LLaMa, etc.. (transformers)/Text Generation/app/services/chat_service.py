from fastapi import FastAPI, HTTPException
from app.core.config import HF_TOKEN, client


def prediction(text: str):
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.2-3B-Instruct:novita",
            messages=[{"role": "user", "content": request.text}]
        )
        return {"response": completion.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Llama model error: {e}")
