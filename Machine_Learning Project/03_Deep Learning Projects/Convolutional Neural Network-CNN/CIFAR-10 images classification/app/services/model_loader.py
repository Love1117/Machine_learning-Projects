import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = keras.models.load_model(MODEL_DIR / "CIFAR-10 images classification/CIFAR-10_images_classification.keras")
print("Model loaded successfully!")
