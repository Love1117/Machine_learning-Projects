import joblib
import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = keras.models.load_model(MODEL_DIR / "Smart_home_EnergyConsumption_Prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
