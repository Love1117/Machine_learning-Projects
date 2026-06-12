from fastapi import File, UploadFile
from PIL import Image
import numpy as np
import io
import os

from app.services.model_loader import model
from app.core.constants import flower_dict
from app.database.crud import save_prediction



def predict_flower_prediction(file: UploadFile = File(...), db):
  try:
    # Read the image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Preprocess the image
    image = image.resize((180, 180))
    image = np.array(image)
    
    # Ensure image has 3 channels if it's grayscale (some PNGs)
    if image.ndim == 2:
        image = np.stack((image,)*3, axis=-1)
    elif image.shape[-1] == 4: # Remove alpha channel if present
        image = image[:, :, :3]

    image = image / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(image)
    predicted_class_idx = np.argmax(prediction)
    predicted_class_name = flower_dict[predicted_class_idx]
    confidence = float(np.max(prediction))

    db_obj = save_prediction("filename": file.filename, "predicted_class": predicted_class_name, "confidence": confidence)

    return {
        "filename": filename,
        "predicted_class": predicted_class_name,
        "confidence": confidence,
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
