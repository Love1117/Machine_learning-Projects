
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import uvicorn
import joblib
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Loan_approval_prediction_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
Loan_intent_freq = joblib.load(MODEL_DIR / "Loan_intent_freq.joblib")
Home_ownership_freq = joblib.load(MODEL_DIR / "Home_ownership_freq.joblib")



app = FastAPI(title="API Loan Approval Prediction",
              description="Production style, FastAPI for Loan Approval Prediction")


@app.get("/model_check")
async def model_status():
  return {"Status":"Okay",
            "Model_loaded": True}

@app.get("/model_info")
async def info():
  return {"Project_name":"Loan Approval Prediction",
          "Features":["Age",
                       "Gender",
                      "Education",
                      "Income",
                      "Employment_experience",
                      "Home_ownership",
                      "Loan_amount",
                      "Loan_intent",
                      "Loan_interest_rate",
                      "Loan_percent_income",
                      "Credit_history_length",
                      "Credit_score",
                      "Previous_loan_defaults_on_file",
                     "Loan_status"],
          "Version": "v1.0.0.0"}


Loan_intent_Enum = Literal[tuple(Loan_intent_freq.keys())]
Home_ownership_Enum = Literal[tuple(Home_ownership_freq.keys())]


GENDER = {"Male":1, "Female":0}
EDUCATION = {"High School":0, "Associate":1, "Bachelor":2, "Master":3, "Doctorate":4}
PREVIOUS_LOAN = {"Yes":1, "No":0}


class Base(BaseModel):
  Age: float= Field(..., example=25, description="Fill in the space")
  Gender: Literal["Male","Female"]
  Education: Literal["High School", "Associate", "Bachelor", "Master", "Doctorate"]
  Income: float= Field(..., example=66135.0, description="Fill in the space")
  Employment_experience:int= Field(..., example=3, description="Fill in the space")
  Home_ownership: Home_ownership_Enum
  Loan_amount: float= Field(..., example=35000.0, description="Fill in the space")
  Loan_intent: Loan_intent_Enum
  Loan_interest_rate: float= Field(..., example=16.02, description="Fill in the space")
  Loan_percent_income: float= Field(..., example=0.53, description="Fill in the space")
  Credit_history_length: float= Field(..., example=3.0, description="Fill in the space")
  Credit_score: int= Field(..., example=617, description="Fill in the space")
  Previous_loan_defaults_on_file: Literal["Yes","No"]


@app.post("/predict")
async def predict(data: Base):
  try:
    Loan_intent_Encoded = Loan_intent_freq[data.Loan_intent]
    Home_ownership_Encoded = Home_ownership_freq[data.Home_ownership]

    Gender_map = GENDER[data.Gender]
    Education_map = EDUCATION[data.Education]
    Previous_loan_map = PREVIOUS_LOAN[data.Previous_loan_defaults_on_file]

    input_data = pd.DataFrame([{"Age":data.Age,
                                "Gender": Gender_map,
                                "Education": Education_map,
                                "Income": data.Income,
                                "Employment_experience": data.Employment_experience,
                                "Home_ownership": Home_ownership_Encoded,
                                "Loan_amount": data.Loan_amount,
                                "Loan_intent": Loan_intent_Encoded,
                                "Loan_interest_rate": data.Loan_interest_rate,
                                "Loan_percent_income": data.Loan_percent_income,
                                "Credit_history_length": data.Credit_history_length,
                                "Credit_score": data.Credit_score,
                                "Previous_loan_defaults_on_file": Previous_loan_map }])

    input_data = input_data[["Age",
                             "Gender",
                             "Education",
                             "Income",
                             "Employment_experience",
                             "Home_ownership",
                             "Loan_amount",
                             "Loan_intent",
                             "Loan_interest_rate",
                             "Loan_percent_income",
                             "Credit_history_length",
                            "Credit_score",
                            "Previous_loan_defaults_on_file"]]
    scaled_input = scale.transform(input_data)

    prediction = model.predict(scaled_input)[0]

    return {"prediction": "Loan_Approved" if prediction == 1 else "Loan_Decline"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
