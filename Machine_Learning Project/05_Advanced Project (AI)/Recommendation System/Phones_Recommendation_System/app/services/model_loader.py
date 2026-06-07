import joblib
from app.core.config import MODEL_DIR


phone_data = joblib.load(MODEL_DIR, "phone_data.joblib")
vector = joblib.load(MODEL_DIR, "vector.joblib")
