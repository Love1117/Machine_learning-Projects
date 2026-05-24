import joblib
from app.core.config import MODEL_DIR


vector = joblib.load(MODEL_DIR / "vector.joblib")
tfidf = joblib.load(MODEL_DIR / "tfidf.joblib")
movies = joblib.load(MODEL_DIR / "movies.joblib")
