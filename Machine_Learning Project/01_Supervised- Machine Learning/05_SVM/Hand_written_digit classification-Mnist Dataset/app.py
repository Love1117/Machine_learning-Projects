
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import numpy as np
import joblib
import io
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Handwritten_digit_v1.0.0.joblib")


app = FastAPI(
        title="Handwritten Digit Image Recognition API",
        version="1.0.0")


@app.get("/")
def home():
  return {"message": "Digit Image Recognition API is running"}

def preprocess_image(image: Image.Image) -> np.ndarray:
  image = image.convert("L")
  # Resize to 8x8

  image = image.resize((8, 8))
  # Convert to numpy

  image_array = np.array(image)
  # Normalize to 0–16 (sklearn digits scale)

  image_array = image_array / 255.0 * 16
  # Flatten

  return image_array.reshape(1, -1)

@app.post("/predict-image")
async def predict_digit_image(file: UploadFile = File(...)):
  if not file.content_type.startswith("image/"):
    raise HTTPException(status_code=400, detail="File must be an image")

  try:
    # Read image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Preprocess
    features = preprocess_image(image)

    # Predict
    prediction = model.predict(features)[0]

    return {
            "predicted_digit": int(prediction),
            }

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
