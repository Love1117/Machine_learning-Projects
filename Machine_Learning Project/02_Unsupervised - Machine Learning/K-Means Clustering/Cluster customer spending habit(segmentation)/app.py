from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel, Field
from typing import Literal
import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Customer-spending-habit_V1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scaler.joblib")

app = FastAPI()

def encode_Profession(Profession_status):
        return {"Profession_Doctor": 1 if Profession_status == "Doctor" else 0,
                "Profession_Engineer": 1 if Profession_status == "Engineer" else 0,
                "Profession_Entertainment": 1 if Profession_status == "Entertainment" else 0,
                "Profession_Executive": 1 if Profession_status == "Executive" else 0,
                "Profession_Healthcare": 1 if Profession_status == "Healthcare" else 0,
                "Profession_Homemaker": 1 if Profession_status == "Homemaker" else 0,
                "Profession_Lawyer": 1 if Profession_status == "Lawyer" else 0,
                "Profession_Marketing": 1 if Profession_status == "Marketing" else 0}


def encode_Variable(Variable_status):
        return {"Var_1_Cat_2": 1 if Variable_status == "cat_2" else 0,
                "Var_1_Cat_3": 1 if Variable_status == "cat_3" else 0,
                "Var_1_Cat_4": 1 if Variable_status == "cat_4" else 0,
                "Var_1_Cat_5": 1 if Variable_status == "cat_5" else 0,
                "Var_1_Cat_6": 1 if Variable_status == "cat_6" else 0,
                "Var_1_Cat_7": 1 if Variable_status == "cat_7" else 0}



GENDER = {"Male":1, "Female":0}
EVER_MARRIED = {"Yes":1, "No":0}
GRADUATED = {"Yes":1, "No":0}


class Base(BaseModel):
  Gender: Literal["Male", "Female"]
  Ever_Married: Literal["Yes", "No"]
  Age: int= Field(..., example=36, description="input your age")
  Graduated: Literal["Yes", "No"]
  Work_Experience: float= Field(..., example=8.0, description="work_experience")
  Spending_Score: int= Field(..., example=3, description="spending score")
  Family_Size: float= Field(..., example=3.0, description="work_experience")
  Profession_status: str= Field(..., example="Doctor", description="profession")
  Variable_status: str= Field(..., example="cat_2", description="input variable")


@app.post("/predict")
async def predict(data: Base):
  try:
    bp_Profession = encode_Profession(data.Profession_status)
    bp_Variable = encode_Variable(data.Variable_status)

    input_data = pd.DataFrame([{"Gender": GENDER[data.Gender],
                                "Ever_Married": EVER_MARRIED[data.Ever_Married],
                                "Age": data.Age,
                                "Graduated": GRADUATED[data.Graduated],
                                "Work_Experience": data.Work_Experience,
                                "Spending_Score": data.Spending_Score,
                                "Family_Size": data.Family_Size,
                                **bp_Profession,
                                **bp_Variable}])

    scaled_df = scale.transform(input_data)

    prediction = model.predict(scaled_df)[0]

    group_mapping = {
        0: "High-Value Loyal Customers",
        1: "Budget-Conscious Shoppers",
        2: "Premium Customers",
        3: "Low Engagement Customers",
        4: "Occasional Spenders",
        5: "Occasional Spenders",
        6: "Impulse / Trend Buyers"
    }
    return {"Group_into": group_mapping.get(prediction, "Unknown Group")}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
