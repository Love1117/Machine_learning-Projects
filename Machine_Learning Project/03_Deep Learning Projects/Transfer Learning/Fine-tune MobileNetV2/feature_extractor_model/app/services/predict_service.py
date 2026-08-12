from fastapi import File, UploadFile, HTTPException
import tensorflow as tf
from PIL import Image
import numpy as np
import io

from app.services.model_loader import loaded_model, class_names
from app.database.crud import save_prediction


# Define image dimensions
img_height = 224
img_width = 224



async def predict_flower(file: UploadFile = File(...), db):
  try:
    # Read the image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).resize((img_height, img_width))

    # Preprocess the image
    img_array = np.array(image).astype('float32') / 255.0 # Normalize
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension

    # Make prediction
    predictions = loaded_model.predict(img_array)
    predicted_class_id = tf.argmax(predictions, axis=-1).numpy()[0]
    predicted_class_name = class_names[predicted_class_id]
    confidence = float(np.max(predictions))

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, filename=file.filename, predicted_class=predicted_class_name, confidence=confidence)
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
        "predicted_class": predicted_class_name,
        "confidence": confidence,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
