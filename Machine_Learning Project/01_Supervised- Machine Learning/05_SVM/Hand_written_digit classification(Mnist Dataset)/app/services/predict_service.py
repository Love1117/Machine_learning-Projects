import pandas as pd
from fastapi import File, UploadFile, HTTPException
from PIL import Image
import numpy as np
import joblib
import io
from pathlib import Path

from app.services.model_loader import model
from app.services.preprocessing import preprocess_image
from app.database.crud import save_prediction


def predict_digit(file, db: Session):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Preprocess
    features = preprocess_image(image)

    # Predict
    prediction = model.predict(features)[0]

    
    db_obj = save_prediction(db, filename, predicted_digit)

    return {
        "predicted_digit": int(prediction),
        "db_id": db_obj.id
    }
