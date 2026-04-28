import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "Employee_salary1_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
Country_freq = joblib.load(MODEL_DIR / "country_freq.joblib")
Race_freq = joblib.load(MODEL_DIR / "race_freq.joblib")
Job_title_encoder = joblib.load(MODEL_DIR / "Job_title_encode.joblib")
