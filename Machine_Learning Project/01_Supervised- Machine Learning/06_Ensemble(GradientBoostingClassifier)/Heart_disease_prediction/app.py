
from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn
from pydantic import BaseModel, Field
from typing import Literal
import joblib
from pathlib import path


BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Heart_disease_v1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale_v1.0.0.joblib")

app = FastAPI()

GENDER = {"Male":1,"Female":0}
PHYSICAL = {"Yes":1, "No":0}
ALCOHOL = {"Yes":1, "No":0}
SMOKE = {"Yes":1, "No":0}

def encode_bp(bp_status):
        return {"bp_Hypertension Stage 1": 1 if bp_status == "stage1" else 0,
                "bp_Hypertension Stage 2": 1 if bp_status == "stage2" else 0,
                "bp_Normal": 1 if bp_status == "normal" else 0,}

class Base(BaseModel):
  gender: Literal["Male","Female"]
  height: float= Field(..., example=168.0, description="what is your height")
  weight: float= Field(..., example=62.0, description="what is your weight")
  systolic_blood_pressure: int= Field(..., example=110, description="input number of systolic blood pressure")
  diastolic_blood_pressure: int= Field(..., example=80, description="input number of diastolic blood pressure")
  cholesterol: int= Field(..., example=1, description="input number of cholesterol")
  gluc: int= Field(..., example=1, description="what is your glucose level")
  smoke: Literal["Yes","No"]
  alcohol_intake: Literal["Yes","No"]
  Physical_activity: Literal["Yes","No"]
  age: int= Field(..., example=50, description="put in your number of age")
  bmi: float= Field(..., example=21.967120, description="fil in bmi" )
  bp_status: str= Field(..., example="stage1", description="what is your blood pressure stage")

@app.post("/predict")
async def predict(data: Base):
  try:
    bp_encoded = encode_bp(data.bp_status)

    input_data = pd.DataFrame([{"gender": GENDER[data.gender],
                    "height": data.height,
                                "weight": data.weight,
                                "systolic_blood_pressure": data.systolic_blood_pressure,
                                "diastolic_blood_pressure": data.diastolic_blood_pressure,
                                "cholesterol": data.cholesterol, # Corrected typo here
                                "gluc": data.gluc,
                                "smoke": SMOKE[data.smoke],
                                "alcohol_intake": ALCOHOL[data.alcohol_intake],
                                "Physical_activity": PHYSICAL[data.Physical_activity],
                                "age": data.age,
                                "bmi": data.bmi,
                                **bp_encoded}])

    scale_df = scale.transform(input_data)

    prediction = model.predict(scale_df)[0]

    return {"Heart Disease: Yes" if prediction == 1 else "Heart Disease: No"}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
