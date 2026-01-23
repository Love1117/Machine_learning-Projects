
from fastapi import FastAPI, HTTPException
import joblib
from typing import Literal
from pydantic import BaseModel, Field
import pandas as pd
from pathlib import Path




BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "House_price_prediction_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
AddressAndCity_Encode = joblib.load(MODEL_DIR / "address_and_city_Encode.joblib")
State_Encode = joblib.load(MODEL_DIR / "state_Encode.joblib")
County_Encode = joblib.load(MODEL_DIR / "county_Encode.joblib")



AddressAndCity_Enun = Literal[tuple(AddressAndCity_Encode.keys())]
County_Enum = Literal[tuple(County_Encode.keys())]
State_Enun = Literal[tuple(State_Encode.keys())]

app = FastAPI(title="House Price Prediction API",
              description="Production Style, Machine learning for house price prediction",
              version="version1.0.0.0")

@app.get("/Health")
async def health_check():
  return {"status":"OK",
          "Model_loaded":True}


@app.get("/Model/{used_model}")
async def Model_Info(used_model: str="Linear_Regression"):
  return {"model":{used_model},
          "Features":["Bedrooms",
                      "Bathrooms",
                      "Living_Space",
                      "Median_Household_Income",
                      "Zip_Code",
                      "Latitude",
                      "Longitude",
                      "Address_And_City",
                      "State",
                      "County",
                      "Price"],
          "Version":"v1.0.0.0"}


class Base(BaseModel):
  Bedrooms: int= Field(..., example=2, description="fill in numbers of bedroom")
  Bathrooms: int= Field(..., example=3, description="fill in numbers of bathroom")
  Living_Space: int= Field(..., example=1538, description="fill in the size of Living Space")
  Median_Household_Income: float= Field(..., example=370046.00, description="Median_Household_Income")
  Zip_Code: float= Field(..., example=10017, description="Zip Code")
  Latitude: float= Field(..., example=40.72, description="Latitude")
  Longitude: float= Field(..., example=-74.00, description="Longitude")
  Address_And_City: AddressAndCity_Enun
  State: State_Enun
  County: County_Enum


@app.post("/predict")
async def predict(data: Base):
  try:
    AddressAndCity_Encoded = AddressAndCity_Encode[data.Address_And_City]
    State_Encoded = State_Encode[data.State]
    County_Encoded = County_Encode[data.County]

    input_data = pd.DataFrame([{"Bedrooms": data.Bedrooms,
                              "Bathrooms": data.Bathrooms,
                              "Living_Space": data.Living_Space,
                              "Median_Household_Income": data.Median_Household_Income,
                              "Zip_Code": data.Zip_Code,
                              "Latitude": data.Latitude,
                              "Longitude": data.Longitude,
                              "Address_And_City": AddressAndCity_Encoded,
                              "State": State_Encoded,
                              "County": County_Encoded}])
    
    input_data = input_data[["Bedrooms",
                             "Bathrooms",
                             "Living_Space",
                             "Median_Household_Income",
                             "Zip_Code",
                             "Latitude",
                             "Longitude",
                             "Address_And_City",
                             "State",
                             "County"]]

    scaled_df = scale.transform(input_data)

    prediction = model.predict(scaled_df)[0]

    return {"Prediction": float(round(prediction,2)),}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
