from fastapi import FastAPI, HTTPException
import uvicorn
import joblib
from pydantic import BaseModel, Field
from typing import Literal
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import models
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = models.load_model(MODEL_DIR / "Customer_churn_prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")


app = FastAPI()

def encode_PaymentMethod(PaymentMethod_status):
        return {"PaymentMethod_Credit card (automatic)": 1 if PaymentMethod_status == "Credit card (automatic)" else 0,
                "PaymentMethod_Electronic check": 1 if PaymentMethod_status == "Electronic check" else 0,
                "PaymentMethod_Mailed check": 1 if PaymentMethod_status == "Mailed check" else 0}

def encode_Contract(Contract_status):
        return {"Contract_One year": 1 if Contract_status == "One year" else 0,
                "Contract_Two year": 1 if Contract_status == "Two year" else 0}


def encode_InternetService(InternetService_status):
        return {"InternetService_DSL": 1 if InternetService_status == "DSL" else 0,
                "InternetService_Fiber optic": 1 if InternetService_status == "Fiber optic" else 0}


GENDER = {"Male":1, "Female":0}
Senior_Citizen = {"Yes":1, "No":0}
PARTNER = {"Yes":1, "No":0}
DEPENDENT = {"Yes":1, "No":0}
Phone_Sevice = {"Yes":1, "No":0}
Multi_Lines = {"Yes":1, "No":0}
Online_Security = {"Yes":1, "No":0}
Online_Backup = {"Yes":1, "No":0}
Device_Protection = {"Yes":1, "No":0}
Tech_Support = {"Yes":1, "No":0}
Streaming_TV = {"Yes":1, "No":0}
Streaming_Movies = {"Yes":1, "No":0}
Peperless_Billings = {"Yes":1, "No":0}



class Base(BaseModel):
  gender: Literal["Male","Female"]
  SeniorCitizen: Literal["Yes","No"]
  Partner: Literal["Yes","No"]
  Dependents: Literal["Yes","No"]
  tenure: int= Field(..., example=1, description="What is your monthly charges")
  PhoneService: Literal["Yes","No"]
  MultipleLines: Literal["Yes","No"]
  OnlineSecurity: Literal["Yes","No"]
  OnlineBackup: Literal["Yes","No"]
  DeviceProtection: Literal["Yes","No"]
  TechSupport: Literal["Yes","No"]
  StreamingTV: Literal["Yes","No"]
  StreamingMovies: Literal["Yes","No"]
  PaperlessBilling: Literal["Yes","No"]
  MonthlyCharges: float= Field(..., example=29.85, description="What's your monthly charges")
  TotalCharges: float= Field(..., example=29.85, description="What's your total charges")
  PaymentMethod_status: str= Field(..., example="Credit card (automatic)", description="Payment method")
  Contract_status: str= Field(..., example="One year", description="Years of contract")
  InternetService_status: str= Field(..., example="DSL", description="Internet Service")

@app.post("/predict")
async def predict(data: Base):
  try:
    PaymentMethod_encode = encode_PaymentMethod(data.PaymentMethod_status)
    Contract_encode = encode_Contract(data.Contract_status)
    InternetService_encode = encode_InternetService(data.InternetService_status)

    input_data = pd.DataFrame([{"gender": GENDER[data.gender],
                                "SeniorCitizen": Senior_Citizen[data.SeniorCitizen],
                                "Partner": PARTNER[data.Partner],
                                "Dependents": DEPENDENT[data.Dependents],
                                "tenure": data.tenure,
                                "PhoneService": Phone_Sevice[data.PhoneService],
                                "MultipleLines": Multi_Lines[data.MultipleLines],
                                "OnlineSecurity": Online_Security[data.OnlineSecurity],
                                "OnlineBackup": Online_Backup[data.OnlineBackup],
                                "DeviceProtection": Device_Protection[data.DeviceProtection],
                                "TechSupport": Tech_Support[data.TechSupport],
                                "StreamingTV": Streaming_TV[data.StreamingTV],
                                "StreamingMovies": Streaming_Movies[data.StreamingMovies],
                                "PaperlessBilling": Peperless_Billings[data.PaperlessBilling],
                                "MonthlyCharges": data.MonthlyCharges,
                                "TotalCharges": data.TotalCharges,
                                **PaymentMethod_encode,
                                **Contract_encode,
                                **InternetService_encode}])

    large = ["tenure","MonthlyCharges","TotalCharges"]

    input_data[large] = scale.transform(input_data[large])

    scaled_df = input_data

    probability = model.predict(scaled_df)[0][0]
    prediction_class = 1 if probability >= 0.5 else 0

    return {"prediction_probability": float(probability),
            "Prediction": "Customer Left" if prediction_class == 1 else "Customer Retained",
            "model_used": "ANN"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
