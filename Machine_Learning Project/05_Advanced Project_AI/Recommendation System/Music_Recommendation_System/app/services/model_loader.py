import joblib
from app.core.config import MODEL_DIR


matrix = joblib.load(MODEL_DIR, "matrix.joblib")
songs = joblib.load(MODEL_DIR, "songs.joblib")