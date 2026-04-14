from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from PIL import Image
import io
import numpy as np
from tensorflow import keras
from pathlib import Path
import joblib


app = FastAPI(title="CIFAR-10 Image Classification API")

model_path = ("/content/drive/My Drive/Models/Deep Learning/Convolutional Neural Network/CIFAR-10 images classification/CIFAR-10_images_classification.keras")

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "CreditCard_fraud_transaction.joblib")

@app.on_event("startup")
async def load_model():
    global model
    model = keras.models.load_model(model_path)
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
