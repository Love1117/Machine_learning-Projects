from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Literal
from pydantic import BaseModel, Field
import joblib
import pandas as pd
from enum import Enum
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "car_price_prediction_V1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
Car_modelAndYear_Encode = joblib.load(MODEL_DIR / "car_ModelAndYear_encode.joblib")
Car_name_Encode = joblib.load(MODEL_DIR / "car_name_encode.joblib")



app = FastAPI(title="Fastapi for Car_price_Prediction",
              description= "Production style, FastAPI for Car price prediction")

@app.get("/model_check")
async def model_status():
  return {"Status": "ok",
          "model_loaded": True}


@app.get("/model_info")
async def model_info():
  return {"model_type":"Linear_Regresion",
          "Features":["car_model",
                      "year",
                      "car_name",
                      "km_driven",
                      "transmission",
                      "millage",
                      "engine",
                      "max_power",
                      "seats",
                      "fuel",
                      "seller_type",
                      "owner",
                      "selling_price"],
          "Version": "v1.0.0.0"}



Transmission_Map = {"Automatic":1, "Manual":0}


Fuel_Columns = ["fuel_Diesel", "fuel_LPG", "fuel_Petrol"]
Owner_Columns = ["owner_Fourth & Above Owner", "owner_Second Owner", "owner_Test Drive Car", "owner_Third Owner"]
Seller_type_Columns = ["seller_type_Individual", "seller_type_Trustmark Dealer"]


Car_modelAndYear_Enum = Literal[tuple(Car_modelAndYear_Encode.keys())]
Car_name_Enum = Literal[tuple(Car_name_Encode.keys())]

class Base(BaseModel):
  car_ModelAndYear: Car_modelAndYear_Enum
  car_name: Car_name_Enum
  year: int = Field(..., example=2018, description="Year of the car")
  km_driven: float = Field(..., example=145500, description="Km_driven by car")
  transmission: Literal["Automatic","Manual"]
  mileage: float = Field(..., example=23.40, description="Mileage of car")
  engine: float = Field(..., example=1248.0, description="Engine capacity of car")
  max_power: float = Field(..., example=74.00		, description="Car maximum power")
  seats: float = Field(..., example=4, description="Car number of seats2")
  
  fuel: Literal["Diesel","Petrol","LPG","CNG"]
  owner: Literal["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"]
  seller_type: Literal["Individual", "Dealer", "Trustmark Dealer"]




def encode_fuel(fuel: str):
  return {col: 1 if col == f"fuel_{fuel}" else 0 for col in Fuel_Columns}

def encode_owner(owner: str):
  return {col: 1 if col == f"owner_{owner}" else 0 for col in Owner_Columns}

def encode_seller_type(seller_type: str):
  return {col: 1 if col == f"seller_type_{seller_type}" else 0 for col in Seller_type_Columns}



@app.post("/predict")
async def predict(data: Base):

  try:
    fuel_encoded = encode_fuel(data.fuel)
    owner_encoded = encode_owner(data.owner)
    seller_type_encoded = encode_seller_type(data.seller_type)

    Car_modelAndYear_List = Car_modelAndYear_Encode[data.car_ModelAndYear]
    Car_name_List = Car_name_Encode[data.car_name]

 
    input_dict = {
        "car_ModelAndYear": Car_modelAndYear_List,
        "car_name": Car_name_List,
        "year": data.year,
        "km_driven": data.km_driven,
        "transmission": Transmission_Map[data.transmission],
        "mileage": data.mileage,
        "engine": data.engine,
        "max_power": data.max_power,
        "seats": data.seats,
        **fuel_encoded,
        **owner_encoded,
        **seller_type_encoded
    }

    
    all_expected_columns = [
        "car_ModelAndYear",
        "car_name",
        "year",
        "km_driven",
        "transmission",
        "mileage",
        "engine",
        "max_power",
        "seats",
    ] + Fuel_Columns + Owner_Columns + Seller_type_Columns

    
    input_data = pd.DataFrame([input_dict]).reindex(columns=all_expected_columns, fill_value=0)

    scaled_input = scale.transform(input_data)

    prediction = model.predict(scaled_input)[0]

    
    return {"Car Price": float(round(prediction, 2)),}


  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
