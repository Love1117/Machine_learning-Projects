from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from PIL import Image
import io
import numpy as np
import tensorflow as tf
from tensorflow import keras


app = FastAPI(title="CIFAR-10 Image Classification API")

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"


@app.on_event("startup")
async def load_model():
    global model
    model = keras.models.load_model(MODEL_DIR / "CreditCard_fraud_transaction.joblib")
    print("Model loaded successfully!")


Classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]


class PredictionResponse(BaseModel):
    filename: str
    predicted_class: str
    confidence: float


@app.post("/predict", response_model=PredictionResponse)
async def predict_image(file: UploadFile = File(...)):
  try:


    image_data = await file.read()
    image = Image.open(io.BytesIO(image_data))

    image = image.resize((32, 32))
    image = image.convert('RGB')
    image = np.asarray(image, dtype=np.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    predicted_class_index = np.argmax(predictions)
    confidence = float(np.max(predictions))
    predicted_class_name = Classes[predicted_class_index]

    return {"filename": file.filename, "predicted_class": predicted_class_name, "confidence": confidence}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
