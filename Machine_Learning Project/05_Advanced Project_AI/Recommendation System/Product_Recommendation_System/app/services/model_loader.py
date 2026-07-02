import joblib
from app.core.config import MODEL_DIR


products = joblib.load(MODEL_DIR / "products.joblib")
vector = joblib.load(MODEL_DIR / "vector.joblib")
