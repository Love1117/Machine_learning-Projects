import joblib
import tensorflow as tf
from tensorflow import keras
from app.core.config import MODEL_DIR

model = keras.models.load_model(MODEL_DIR / "Insurance-ownership-prediction.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
