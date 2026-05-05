import joblib
from app.core.config import MODEL_DIR

model = models.load_model(MODEL_DIR / "Insurance-ownership-prediction.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")
