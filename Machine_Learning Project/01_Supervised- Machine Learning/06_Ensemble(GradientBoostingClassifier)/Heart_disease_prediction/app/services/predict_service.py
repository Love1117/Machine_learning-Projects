import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_bp
from app.core.constants import SMOKE. ALCOHOL, PHYSICAL, GENDER 
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    bp_encode = encode_bp(data.bp_status)

    input_data = pd.DataFrame([{"gender": GENDER[data.gender],
                                "height": data.height,
                                "weight": data.weight,
                                "systolic_blood_pressure": data.systolic_blood_pressure,
                                "diastolic_blood_pressure": data.diastolic_blood_pressure,
                                "cholesterol": data.cholesterol, # Corrected typo here
                                "gluc": data.gluc,
                                "smoke": SMOKE[data.smoke],
                                "alcohol_intake": ALCOHOL[data.alcohol_intake],
                                "Physical_activity": PHYSICAL[data.Physical_activity],
                                "age": data.age,
                                "bmi": data.bmi,
                                **bp_encoded}])

    scale_df = scale.transform(input_data)

    prediction = model.predict(scale_df)[0]

    db_obj = save_prediction(db, data, prediction)

    return {
        "Heart Disease: Yes" if prediction == 1 else "Heart Disease: No",
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
