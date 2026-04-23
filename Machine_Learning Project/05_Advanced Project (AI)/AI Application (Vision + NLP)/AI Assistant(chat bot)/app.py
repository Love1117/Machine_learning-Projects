from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from typing import Optional
import uvicorn
import nest_asyncio
import io
import base64
from PIL import Image
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN,
)

nest_asyncio.apply()

app = FastAPI()


# Encode image
def encode_image(img_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(img_bytes))
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


@app.post("/chat")
async def chat_with_model(
    question: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    try:
        content = [{"type": "text", "text": question}]

        # Handle image if present
        if image:
            image_bytes = await image.read()
            image_b64 = encode_image(image_bytes)

            content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_b64}"
                }
            })

        response = client.chat.completions.create(
            model="google/gemma-3-27b-it",
            messages=[
                {"role": "user", "content": content}
            ],
            max_tokens=200
        )

        return {
            "response": response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
