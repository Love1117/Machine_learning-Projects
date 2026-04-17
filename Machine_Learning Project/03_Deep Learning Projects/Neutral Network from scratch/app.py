from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
import pandas as pd
import uvicorn
from typing import Literal
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = models.load_model(MODEL_DIR / "Neural-Network-from-Scratch.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")

app = FastAPI()

Gender = {"Male":1, "Female":0}
SMOKER = {"Yes":1, "No":0}
class InsuranceFeatures(BaseModel):
    age: int = Field(..., example=19, description="Age")
    sex: Literal["Male","Female"]
    bmi: float = Field(..., example=27.900, description="Bmi")
    children: int = Field(..., example=0, description="Children")
    smoker: Literal["Yes","No"]
    region: int = Field(..., example=3, description="Region")
    charges: float = Field(..., example=16884.92400, description="Charges")

@app.post("/predict_ann_claim/")
async def predict_ann_claim(features: InsuranceFeatures):
  try:
    input_data = pd.DataFrame([{"age": features.age,
                                "sex": Gender[features.sex],
                                "bmi": features.bmi,
                                "children": features.children,
                                "smoker": SMOKER[features.smoker],
                                "region": features.region,
                                "charges": features.charges,}])

    scaled_input_data = scale.transform(input_data)

    prediction_proba = model.predict(scaled_input_data)[0][0]
    prediction_class = int(np.round(prediction_proba))

    return {"prediction_probability": float(prediction_proba),
            "predicted_insurance_claim": "Has Insurance" if prediction_class ==1 else "No Insurance",
            "model_used": "ANN"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
