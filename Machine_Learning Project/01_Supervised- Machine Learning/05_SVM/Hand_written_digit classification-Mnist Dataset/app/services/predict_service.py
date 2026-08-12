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


async def predict_digit(file: UploadFile, db):
  try:
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Preprocess
    features = preprocess_image(image)

    # Predict
    prediction = model.predict(features)[0]
    predicted_digit = int(prediction)

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, filename=file.filename, predicted_digit=predicted_digit)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass

    return {
        "predicted_digit": int(prediction),
        "filename": file.filename,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
