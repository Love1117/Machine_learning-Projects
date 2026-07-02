import joblib
import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = keras.models.load_model(MODEL_DIR / "Fraud_detection_prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
