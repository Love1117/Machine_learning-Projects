import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "Heart_disease_v1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale_v1.0.0.joblib")
