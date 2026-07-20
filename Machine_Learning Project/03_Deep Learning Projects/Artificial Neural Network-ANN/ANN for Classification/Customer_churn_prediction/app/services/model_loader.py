import os
import joblib
from tensorflow import keras
from app.core.config import MODEL_DIR

print("MODEL_DIR:", MODEL_DIR)
print("Exists:", MODEL_DIR.exists())

print("Files:")
if MODEL_DIR.exists():
    print(os.listdir(MODEL_DIR))

model = keras.models.load_model(
    MODEL_DIR / "Customer_churn_prediction_V1.0.0.keras"
)

scale = joblib.load(
    MODEL_DIR / "scale.joblib"
)
