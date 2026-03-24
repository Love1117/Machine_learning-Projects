from fastapi import FastAPI, HTTPException
import uvicorn
import pandas as pd
from pydantic import BaseModel, Field
from pathlib import Path
import joblib



app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

model = joblib.load(MODEL_DIR / "CreditCard_fraud_transaction.joblib")
scale = joblib.load(MODEL_DIR / "scale.joblib")



def encode_type(type_status):
          return {"type_CASH_OUT": 1 if type_status == "CASH_OUT" else 0,
                  "type_DEBIT": 1 if type_status == "DEBIT" else 0,
                  "type_PAYMENT": 1 if type_status == "PAYMENT" else 0,
                  "type_TRANSFER": 1 if type_status == "TRANSFER" else 0}




class Base(BaseModel):
  step: float= Field(..., json_schema_extra={"example": 183, "description": "Input number of steps"})
  amount: float = Field (..., json_schema_extra={"example": 22004.84, "description": "Amount"})
  oldbalanceOrg: float = Field (..., json_schema_extra={"example": 87956.18, "description": "Old balance of originator account"})
  newbalanceOrig: float = Field (..., json_schema_extra={"example": 65951.34, "description": "New balance of originator account"})
  oldbalanceDest: float = Field (..., json_schema_extra={"example": 0.00, "description": "Old balance of destination account"})
  newbalanceDest: float = Field (..., json_schema_extra={"example": 0.00, "description": "New balance of destination account"})
  type_status: str = Field (..., json_schema_extra={"example": "CASH_OUT", "description": "Type of payment"})

@app.post("/predict")
async def predict(data: Base):
  try:
    type_encoded = encode_type(data.type_status)

    input_data = pd.DataFrame([{"step": data.step,
                                  "amount": data.amount,
                                  "oldbalanceOrg": data.oldbalanceOrg,
                                  "newbalanceOrig": data.newbalanceOrig,
                                  "oldbalanceDest": data.oldbalanceDest,
                                  "newbalanceDest": data.oldbalanceDest,
                                  **type_encoded}])

    scale_df = scale.transform(input_data)

    prediction = model.predict(scale_df)[0]

    return {"is_fraud: Yes" if prediction == -1 else "is_fraud:: No"}

  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
