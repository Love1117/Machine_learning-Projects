import joblib
from app.core.config import MODEL_DIR

tfidf_vectorizer = joblib.load(MODEL_DIR / "tfidf_vectorizer.joblib")
model = joblib.load(MODEL_DIR / "Email-spam-detection_V1.0.0.joblib")
