import joblib
from app.core.config import MODEL_DIR

model = models.load_model(MODEL_DIR / "Smart_home_EnergyConsumption_Prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
