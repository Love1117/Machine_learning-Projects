import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "car_price_prediction_V1.0.0.0.joblib")
scaler = joblib.load(MODEL_DIR / "scale.joblib")
car_model_encoder = joblib.load(MODEL_DIR / "car_ModelAndYear_encode.joblib")
car_name_encoder = joblib.load(MODEL_DIR / "car_name_encode.joblib")
