import pandas as pd
from fastapi import File, UploadFile, HTTPException
from PIL import Image
import numpy as np
import joblib
import io
from pathlib import Path

from app.services.model_loader import model
from app.core.constants import Classes
from app.database.crud import save_prediction


def predict_image(file: UploadFile = File(...)):
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

    db_obj = save_prediction("filename": file.filename, "predicted_class_name": predicted_class_name, "confidence": confidence)

    return {
        "predicted_class_name": predicted_class_name,
        "confidence": confidence,
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
