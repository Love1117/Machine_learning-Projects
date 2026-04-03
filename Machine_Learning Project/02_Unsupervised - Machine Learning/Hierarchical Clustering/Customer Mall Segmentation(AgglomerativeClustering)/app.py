from fastapi import FastAPI, HTTPException
import uvicorn
import pandas as pd
from pydantic import BaseModel, Field
from pathlib import Path
import joblib



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "Customer_Mall_Segmentation-V1.0.0.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")



app = FastAPI()

GENDER = {"Male":1, "Female":0}

class Base(BaseModel):
  Gender: Literal["Male", "Female"]
  Age: int= Field(..., example=44, description="input your age")
  Annual_Income_k: float= Field(..., alias="Annual_Income_(k$)", example=73, description="what is your annual income")
  Spending_Score_1_100: float= Field(..., alias="Spending_Score(1-100)", example=7, description="what is your spending score")


@app.post("/predict")
async def predict(data: Base):
  try:
    input_data = pd.DataFrame([{"Gender": GENDER[data.Gender],
                                "Age": data.Age,
                                "Annual Income (k$)": data.Annual_Income_k,
                                "Spending Score (1-100)": data.Spending_Score_1_100}])

    scaled_df = scale.transform(input_data)

    prediction = model.predict(scaled_df)[0]

    group_mapping = {
        0:"High-income, Low-spending customers",
        1:"Average-income, Moderate-spending customers",
        2: "High-income, High-spending customers",
        3: "Low-income, High-spending customers",
        4: "Low-income, Low-spending customers"}

    return {"Falls_Into": group_mapping.get(prediction, "Unknown Group")}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
