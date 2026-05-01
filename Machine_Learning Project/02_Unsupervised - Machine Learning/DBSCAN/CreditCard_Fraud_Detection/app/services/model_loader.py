import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "CreditCard_fraud_transaction.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
