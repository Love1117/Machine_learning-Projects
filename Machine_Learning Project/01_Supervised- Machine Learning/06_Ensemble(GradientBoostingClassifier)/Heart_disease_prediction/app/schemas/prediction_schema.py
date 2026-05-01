from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
    gender: Literal["Male","Female"]
    height: float= Field(..., example=168.0, description="what is your height")
    weight: float= Field(..., example=62.0, description="what is your weight")
    systolic_blood_pressure: int= Field(..., example=110, description="input number of systolic blood pressure")
    diastolic_blood_pressure: int= Field(..., example=80, description="input number of diastolic blood pressure")
    cholesterol: int= Field(..., example=1, description="input number of cholesterol")
    gluc: int= Field(..., example=1, description="what is your glucose level")
    smoke: Literal["Yes","No"]
    alcohol_intake: Literal["Yes","No"]
    Physical_activity: Literal["Yes","No"]
    age: int= Field(..., example=50, description="put in your number of age")
    bmi: float= Field(..., example=21.967120, description="fil in bmi" )
    bp_status: Literal["stage1", "stage2", "normal"]
