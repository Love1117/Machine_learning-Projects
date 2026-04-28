import joblib
from app.core.config import MODEL_DIR

model = joblib.load(MODEL_DIR / "House_price_prediction_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
AddressAndCity_Encoder = joblib.load(MODEL_DIR / "address_and_city_Encode.joblib")
State_Encoder = joblib.load(MODEL_DIR / "state_Encode.joblib")
County_Encoder = joblib.load(MODEL_DIR / "county_Encode.joblib")
