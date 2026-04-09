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

model = models.load_model(MODEL_DIR / "Fraud_detection_prediction_V1.0.0.keras")
scale = joblib.load(MODEL_DIR / "scale.joblib")


app = FastAPI()

def encode_device_type(device_type_status):
        return {"device_type_Mobile": 1 if device_type_status == "Mobile" else 0,
                "device_type_Tablet": 1 if device_type_status == "Tablet" else 0}

def encode_device_ip_reputation(device_ip_reputation_status):
        return {"device_ip_reputation_Good": 1 if device_ip_reputation_status == "Good" else 0,
                "device_ip_reputation_Suspicious": 1 if device_ip_reputation_status == "Suspicious" else 0}


def encode_browser(browser_status):
        return {"browser_Edge": 1 if browser_status == "Edge" else 0,
                "browser_Firefox": 1 if browser_status == "Firefox" else 0,
                "browser_Opera": 1 if browser_status == "Opera" else 0,
                "browser_Safari": 1 if browser_status == "Safari" else 0}


def encode_operating_system(operating_system_status):
        return {"operating_system_Linux": 1 if operating_system_status == "Linux" else 0,
                "operating_system_Windows": 1 if operating_system_status == "Windows" else 0,
                "operating_system_iOS": 1 if operating_system_status == "iOS" else 0,
                "operating_system_macOS": 1 if operating_system_status == "macOS" else 0}


def encode_ad_position(ad_position_status):
        return {"ad_position_Side": 1 if ad_position_status == "Side" else 0,
                "ad_position_Top": 1 if ad_position_status == "Top" else 0}




VPN_USAGE = {"Yes":1, "No":0}
PROXY_USAGE = {"Yes":1, "No":0}
WEEKEND = {"Yes":1, "No":0}



class Base(BaseModel):
  click_duration: float= Field(..., example=0.29, description="Click duration")
  scroll_depth: float= Field(..., example=60, description="Scroll depth")
  mouse_movement: float= Field(..., example=111, description="Mouse movement")
  keystrokes_detected: int= Field(..., example=8, description="What is your monthly charges")
  click_frequency: float= Field(..., example=7, description="Click frequency")
  time_since_last_click: float= Field(..., example=72, description="Time since last click")
  VPN_usage: Literal["Yes","No"]
  proxy_usage: Literal["Yes","No"]
  bot_likelihood_score: float= Field(..., example=0.29, description="Bot likelihood score")
  year: int= Field(..., example=2024, description="What year")
  month: int= Field(..., example=8, description="What month")
  day: int= Field(..., example=23, description="What day")
  days_of_the_week: int= Field(..., example=4, description="days of the week")
  hour: float= Field(..., example=2, description="Which hour")
  weekend: Literal["Yes","No"]
  device_type_status: str= Field(..., example="Mobile", description="Device type")
  device_ip_reputation_status: str= Field(..., example="Good", description="Device ip reputation")
  browser_status: str= Field(..., example="Edge", description="What browser")
  operating_system_status: str= Field(..., example="Linux", description="Operating system")
  ad_position_status: str= Field(..., example="Side", description="ad position")

@app.post("/predict")
async def predict(data: Base):
  try:
    device_type_encode = encode_device_type(data.device_type_status)
    device_ip_reputation_encode = encode_device_ip_reputation(data.device_ip_reputation_status)
    browser_encode = encode_browser(data.browser_status)
    operating_system_encode = encode_operating_system(data.operating_system_status)
    ad_position_encode = encode_ad_position(data.ad_position_status)



    input_data = pd.DataFrame([{"click_duration": data.click_duration,
                                "scroll_depth": data.scroll_depth,
                                "mouse_movement": data.mouse_movement,
                                "keystrokes_detected": data.keystrokes_detected,
                                "click_frequency": data.click_frequency,
                                "time_since_last_click": data.time_since_last_click,
                                "VPN_usage": VPN_USAGE[data.VPN_usage],
                                "proxy_usage": PROXY_USAGE[data.proxy_usage],
                                "bot_likelihood_score": data.bot_likelihood_score,
                                "year": data.year,
                                "month": data.month,
                                "day": data.day,
                                "days_of_the_week": data.days_of_the_week,
                                "hour": data.hour,
                                "weekend": WEEKEND[data.weekend],
                                **device_type_encode,
                                **device_ip_reputation_encode,
                                **browser_encode,
                                **operating_system_encode,
                                **ad_position_encode}])


    scaled_df = scale.transform(input_data)


    probability = model.predict(scaled_df)[0][0]
    prediction_class = 1 if probability >= 0.5 else 0

    return {"is_fraudulent": "Yes" if prediction_class == 1 else "No"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
