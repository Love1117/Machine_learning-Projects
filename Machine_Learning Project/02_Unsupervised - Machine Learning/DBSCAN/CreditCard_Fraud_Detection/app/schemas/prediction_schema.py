from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  step: float= Field(..., json_schema_extra={"example": 183, "description": "Input number of steps"})
  amount: float = Field (..., json_schema_extra={"example": 22004.84, "description": "Amount"})
  oldbalanceOrg: float = Field (..., json_schema_extra={"example": 87956.18, "description": "Old balance of originator account"})
  newbalanceOrig: float = Field (..., json_schema_extra={"example": 65951.34, "description": "New balance of originator account"})
  oldbalanceDest: float = Field (..., json_schema_extra={"example": 0.00, "description": "Old balance of destination account"})
  newbalanceDest: float = Field (..., json_schema_extra={"example": 0.00, "description": "New balance of destination account"})
  type_status: str = Field (..., json_schema_extra={"example": "CASH_OUT", "description": "Type of payment"})
