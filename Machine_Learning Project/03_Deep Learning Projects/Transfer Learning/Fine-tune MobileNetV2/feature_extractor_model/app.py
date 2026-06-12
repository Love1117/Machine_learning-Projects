import tensorflow as tf
from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
import io
import tensorflow_hub as hub
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"


# Define image dimensions
img_height = 224
img_width = 224

feature_extractor_model_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/feature_vector/4"

# Load the TensorFlow Hub module (SavedModel) directly
feature_extractor_module = hub.load(feature_extractor_model_url)

# Wrap the loaded module's call method in a Keras Lambda layer
# This ensures it operates correctly with symbolic KerasTensors
feature_extractor_layer = tf.keras.layers.Lambda(
    lambda x: feature_extractor_module(x, training=False), # Explicitly set training=False for inference
    name='feature_extractor_lambda_layer' # Naming for clarity
)

# Load class names
class_names = joblib.load(MODEL_DIR / "class_names.keras")
num_classes = len(class_names)

# Build the new model using the Functional API
inputs = tf.keras.Input(shape=(img_height, img_width, 3))
x = feature_extractor_layer(inputs)
# Assuming a dense classification head was added after the feature extractor
outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

# Create the functional model
loaded_model = tf.keras.Model(inputs, outputs)

# Load the weights from the saved .keras file into the newly constructed model
# This assumes the architecture of the new model matches the saved model's layers.
loaded_model.load_weights(MODEL_DIR / "Flower_photo-feature-extractor-model.keras")
# -----------------------------------------------------------------------------------


# Initialize FastAPI app
app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
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

    return {"filename": file.filename, "predicted_class": predicted_class_name, "confidence": confidence}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
