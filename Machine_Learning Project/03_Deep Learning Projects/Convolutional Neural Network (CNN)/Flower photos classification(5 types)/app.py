from fastapi import FastAPI, File, UploadFile
from PIL import Image
import numpy as np
import tensorflow as tf
import io
import os
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = tf.keras.models.load_model(MODEL_DIR / "flower_classifier.keras")




app = FastAPI()

# Define the flower dictionary (must match your training order)
flower_dict = {
    0: 'daisy',
    1: 'dandelion',
    2: 'roses',
    3: 'sunflowers',
    4: 'tulips'
}

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Flower Classifier API! Visit /docs for API documentation."}

@app.post("/predict/")
async def predict_flower(file: UploadFile = File(...)):
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

    return {"filename": file.filename, "predicted_class": predicted_class_name, "confidence": confidence}
