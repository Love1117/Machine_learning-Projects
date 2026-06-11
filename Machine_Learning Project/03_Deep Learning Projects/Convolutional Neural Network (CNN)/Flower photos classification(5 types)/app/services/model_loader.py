import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = keras.models.load_model(MODEL_DIR / "flower_classifier.keras")
print("Model loaded successfully!")
