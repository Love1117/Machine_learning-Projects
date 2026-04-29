import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "iris_flower_v1.0.0.joblib")
