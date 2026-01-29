from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

model = joblib.load("/content/drive/My Drive/Models/Iris Flower data/iris_flower_v1.0.0.joblib")

app = FastAPI(title= "FastAPI for iris Flower type prediction",
              version="v1.0.0")

@app.get("/model_check")
async def check_model_status():
  return {"Model_Status": "Okay",
          "Load Model": True}

@app.get("/model_info")
async def info():
  return {"Project_name": "Iris Flower type prediction based on petal, sepal (length and weight)",
          "Features": ["sepal length (cm)",
                        "sepal width (cm)",
                        "petal length (cm)",
                        "petal width (cm)",
                        "target"],
           "Version": "v1.0.0"}

class Base(BaseModel):
  sepal_length: float
  sepal_width: float
  petal_length: float
  petal_width: float

@app.post("/predict")
async def predict(data: Base):
  try:
    input_data = pd.DataFrame([{"sepal length (cm)": data.sepal_length,
                                "sepal width (cm)": data.sepal_width,
                                "petal length (cm)": data.petal_length,
                                "petal width (cm)": data.petal_width}])
    
    prediction = model.predict(input_data)[0]

    if prediction==0:
      iris_flower = "Setosa"

    elif prediction==1:
      iris_flower = "Versicolor"

    else:
      iris_flower = "Verginca"

    return {"prediction": iris_flower}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
