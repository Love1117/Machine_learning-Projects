from fastapi import File, UploadFile, HTTPException
import tensorflow as tf
from PIL import Image
import numpy as np
import io

from app.services.model_loader import classifier_loaded
from app.database.crud import save_prediction


# Define image dimensions
IMAGE_SHAPE = (224, 224)

# Load ImageNet labels for prediction interpretation, as this is an ImageNet classifier
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())


        
async def image_prediction(file: UploadFile, db):
    try:
        # Read the image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB").resize(IMAGE_SHAPE)

        # Preprocess the image
        image_array = np.array(image) / 255.0
        image_batch = np.expand_dims(image_array, axis=0)

        # Make prediction
        result = classifier_loaded.predict(image_batch)

        # Get predicted class and confidence using ImageNet labels
        predicted_class_id = tf.math.argmax(result[0], axis=-1).numpy() # Get the class ID as a Python integer
        predicted_label = imagenet_labels[predicted_class_id] # Directly use the string label from the array
        confidence = float(np.max(result))

        db_id = None
        database_saved = False
    
        try:
            db_obj = save_prediction(db, filename=file.filename, prediction=predicted_label, confidence=confidence)
            db_id = db_obj.id
            database_saved = True
     
        except Exception as db_error:
            traceback.print_exc()
            try:
                db.rollback()
            except Exception:
                pass

        
        return {"filename": file.filename, 
            "prediction": predicted_label, 
            "confidence": confidence,
            "db_id": db_id,
            "database_saved": database_saved}
      
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
