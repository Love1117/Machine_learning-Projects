import joblib
import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = models.load_model(MODEL_DIR / "Neural-Network-from-Scratch.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
