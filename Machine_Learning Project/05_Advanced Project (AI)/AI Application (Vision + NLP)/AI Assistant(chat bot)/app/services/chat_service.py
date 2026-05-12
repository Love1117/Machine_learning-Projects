from fastapi import FastAPI, HTTPException
from app.core.config import HF_TOKEN, client 
from app.services.preprocessing import encode_image


def predict_chat(question, image):  
  try:
    content = [{"type": "text", "text": question}]

    # Handle image if present
    if image:
        image_bytes = await image.read()
        image_b64 = encode_image(image_bytes)

        content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{image_b64}"}})

    response = client.chat.completions.create(
            model="google/gemma-3-27b-it",
            messages=[
                {"role": "user", "content": content}],
            max_tokens=200)
      
    return {
            "response": response.choices[0].message.content
        }
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"Llama model error: {e}")
