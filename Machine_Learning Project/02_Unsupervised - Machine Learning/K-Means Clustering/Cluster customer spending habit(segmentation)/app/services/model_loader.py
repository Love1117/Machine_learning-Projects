import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "Customer-spending-habit_V1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scaler.joblib")
