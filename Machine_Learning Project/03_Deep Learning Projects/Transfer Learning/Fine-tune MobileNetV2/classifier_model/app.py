from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import io
import uvicorn
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

# Initialize FastAPI app
app = FastAPI()

# Define image dimensions
IMAGE_SHAPE = (224, 224)

# Define the exact TF Hub URL for the classifier model as provided by the user
classifier_model_url = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"

# Keras 3 Compatible Model Reconstruction:
# 1. Load the TensorFlow Hub module (tf.Module) directly using hub.load()
loaded_tfhub_module = hub.load(classifier_model_url)

# 2. Wrap the loaded tf.Module's call method in a tf.keras.layers.Lambda layer.
# This makes the TF Hub module compatible with Keras 3's layer system by treating it
# as a regular Keras layer within the Sequential model.
classifier_lambda_layer = tf.keras.layers.Lambda(
    lambda inputs: loaded_tfhub_module(inputs),
    name='tfhub_mobilenet_v2_classifier_lambda_layer'
)

# 3. Build a Keras Sequential model using this Lambda layer.
# This model effectively replicates the user's original Sequential model built with KerasLayer
# but in a Keras 3 compatible way.
classifier_loaded = tf.keras.Sequential([
    tf.keras.Input(shape=IMAGE_SHAPE + (3,)),
    classifier_lambda_layer
])

# 4. Load ONLY the weights from the saved .keras file into the newly constructed model.
# This step ensures that any training or fine-tuning performed on your original model
# is applied to this newly built, Keras 3-compatible model. This bypasses the
# KerasLayer deserialization issue when using `tf.keras.models.load_model`.
try:
    classifier_loaded.load_weights(MODEL_DIR / "my_image_classifier.keras")

except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load weights from {model_save_path}. Please ensure the model architecture matches the TF Hub model. Error: {e}")

# Load ImageNet labels for prediction interpretation, as this is an ImageNet classifier
labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Read the image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).resize(IMAGE_SHAPE)

        # Preprocess the image
        image_array = np.array(image) / 255.0
        image_batch = np.expand_dims(image_array, axis=0)

        # Make prediction
        result = classifier_loaded.predict(image_batch)

        # Get predicted class and confidence using ImageNet labels
        predicted_class_id = tf.math.argmax(result[0], axis=-1).numpy() # Get the class ID as a Python integer
        predicted_label = imagenet_labels[predicted_class_id] # Directly use the string label from the array
        confidence = float(np.max(result))

        return {"filename": file.filename, "prediction": predicted_label, "confidence": confidence}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
