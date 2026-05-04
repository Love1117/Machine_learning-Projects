import joblib
from app.core.config import MODEL_DIR

model = models.load_model(MODEL_DIR / "Fraud_detection_prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
