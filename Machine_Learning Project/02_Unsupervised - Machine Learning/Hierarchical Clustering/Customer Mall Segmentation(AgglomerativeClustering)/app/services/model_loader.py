import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "Customer_Mall_Segmentation-V1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
