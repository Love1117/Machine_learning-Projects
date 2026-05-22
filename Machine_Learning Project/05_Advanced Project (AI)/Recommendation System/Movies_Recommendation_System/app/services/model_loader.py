import joblib
from app.core.config import MODEL_DIR


vector = joblib.load(MODEL_DIR / "Vector.joblib")
similarity = joblib.load(MODEL_DIR / "similarity.joblib")
movies = joblib.load(MODEL_DIR / "movies.joblib")
