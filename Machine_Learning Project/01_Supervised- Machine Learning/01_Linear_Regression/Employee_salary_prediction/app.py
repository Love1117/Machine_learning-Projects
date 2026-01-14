
from fastapi import FastAPI, HTTPException
import uvicorn
from typing import Literal
import joblib
from pydantic import BaseModel
from enum import Enum
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Employee_salary1_v1.0.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")
Country_freq = joblib.load(MODEL_DIR / "country_freq.joblib")
Race_freq = joblib.load(MODEL_DIR / "race_freq.joblib")
Job_title_encode = joblib.load(MODEL_DIR / "Job_title_encode.joblib")



CountryEnum = Literal[tuple(Country_freq.keys())]
RaceEnum = Literal[tuple(Race_freq.keys())]
JobTitleEnum = Literal[tuple(Job_title_encode.keys())]




app = FastAPI(title="Employee Salary Prediction",
              description="Production Style, ML Project for Employees Salary Prediction",
              version= "v1.0.0")


@app.get("/health")
def health_check():
  return {
    "status": "ok",
    "model_loaded": True}


@app.get("/model/info")
def model_info():
  return {
          "model_type": "Linear Regression",
            "features": ["Age",
                         "Gender",
                         "Education_Level",
                         "Year_of_Experience",
                         "Country",
                         "Race",
                         "Senior",
                         "Job_title",
                         "Salary"],
          "Version": "V1.0.0.0"}


Gend = {"Male":1, "Female":0}

class Base(BaseModel):
  Age: float
  Gender: Literal["Male","Female"]
  Education_Level: int
  Years_of_Experience: float
  Country: CountryEnum
  Race: RaceEnum
  Senior: int
  Job_title: JobTitleEnum

@app.post("/predict")
async def predict(data: Base):
  try:
    input_data = pd.DataFrame([{"Age": data.Age,
                                "Gender": Gend[data.Gender],
                                "Education_Level": data.Education_Level,
                                "Years_of_Experience": data.Years_of_Experience,
                                "Country": Country_freq.get(data.Country),
                                "Race": Race_freq.get(data.Race),
                                "Senior": data.Senior,
                                "Job_title": Job_title_encode.get(data.Job_title)}])
    input_data = input_data[["Age",
                             "Gender",
                             "Education_Level",
                             "Years_of_Experience",
                             "Country",
                             "Race",
                             "Senior",
                             "Job_title"]]

    Scale = scale.transform(input_data)

    prediction = model.predict(Scale)[0]

    return {
            "predicted_salary": round(float(prediction), 2)
 }

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
