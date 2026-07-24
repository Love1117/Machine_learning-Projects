import joblib
from app.core.config import MODEL_DIR

model = None
scale = joblib.load(MODEL_DIR / "scale.joblib")
