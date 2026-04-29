import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "Loan_approval_prediction_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
Loan_intent_freq = joblib.load(MODEL_DIR / "Loan_intent_freq.joblib")
Home_ownership_freq = joblib.load(MODEL_DIR / "Home_ownership_freq.joblib")
