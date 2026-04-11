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

model = models.load_model(MODEL_DIR / "Smart_home_EnergyConsumption_Prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")


app = FastAPI()

def encode_Appliance_Type(Appliance_Type_status):
        return {"Appliance_Type_Computer": 1 if Appliance_Type_status == "Computer" else 0,
                "Appliance_Type_Dishwasher": 1 if Appliance_Type_status == "Dishwasher" else 0,
                "Appliance_Type_Fridge": 1 if Appliance_Type_status == "Fridge" else 0,
                "Appliance_Type_Heater": 1 if Appliance_Type_status == "Heater" else 0,
                "Appliance_Type_Lights": 1 if Appliance_Type_status == "Lights" else 0,
                "Appliance_Type_Microwave": 1 if Appliance_Type_status == "Microwave" else 0,
                "Appliance_Type_Oven": 1 if Appliance_Type_status == "Oven" else 0,
                "Appliance_Type_TV": 1 if Appliance_Type_status == "TV" else 0,
                "Appliance_Type_Washing Machine": 1 if Appliance_Type_status == "Washing Machine" else 0}


def encode_Season(Season_status):
        return {"Season_Spring": 1 if Season_status == "Spring" else 0,
                "Season_Summer": 1 if Season_status == "Summer" else 0,
                "Season_Winter": 1 if Season_status == "Winter" else 0}



WEEKEND = {"Yes":1, "No":0}



class Base(BaseModel):
  Home_ID: int= Field(..., example=94, description="Home_ID")
  Outdoor_Temperature_C: float= Field(..., example=-1.0, description="Outdoor_Temperature_(°C)") # Corrected field name
  Household_Size: float= Field(..., example=2, description="Household size")
  Year: int= Field(..., example=2023, description="Year")
  Month: int= Field(..., example=12, description="Month")
  Day: int= Field(..., example=2, description="Month")
  Days_Of_The_Week: int= Field(..., example= 5, description="Days_Of_The_Week")
  Hour: float= Field(..., example=21, description="Hour")
  Weekend: Literal["Yes","No"]
  Appliance_Type_status: str= Field(..., example="Dishwasher", description="Appliance_Type")
  Season_status: str= Field(..., example="Spring", description="Season")


@app.post("/predict")
async def predict(data: Base):
  try:
    Appliance_Type_encode = encode_Appliance_Type(data.Appliance_Type_status)
    Season_encode = encode_Season(data.Season_status)


    input_data = pd.DataFrame([{"Home_ID": data.Home_ID,
                                "Outdoor_Temperature_(°C)": data.Outdoor_Temperature_C, # Corrected key and reference
                                "Household_Size": data.Household_Size,
                                "Year": data.Year,
                                "Month": data.Month,
                                "Day": data.Day,
                                "Days_Of_The_Week": data.Days_Of_The_Week,
                                "Hour": data.Hour,
                                "Weekend": WEEKEND[data.Weekend],
                                **Appliance_Type_encode,
                                **Season_encode}])


    scaled_df = scale.transform(input_data)


    prediction = model.predict(scaled_df)[0][0]

    return {"Energy_Consumption_(kWh)": f"{prediction:.2f}"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
