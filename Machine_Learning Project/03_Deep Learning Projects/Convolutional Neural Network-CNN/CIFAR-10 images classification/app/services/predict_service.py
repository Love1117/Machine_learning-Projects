from fastapi import File, UploadFile, HTTPException
from PIL import Image
import numpy as np
import io
from pathlib import Path

from app.services.model_loader import model
from app.core.constants import Classes
from app.database.crud import save_prediction


async def predict_image(file: UploadFile, db):
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


    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, filename=file.filename, predicted_class_name=predicted_class_name, confidence=confidence)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass
          
    return {
        "filename": file.filename,
        "predicted_class_name": predicted_class_name,
        "confidence": confidence,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
