import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_bp
from app.core.constants import SMOKE, ALCOHOL, PHYSICAL, GENDER 
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
                                **bp_encode}])

    scale_df = scale.transform(input_data)

    prediction = model.predict(scale_df)[0]
    Heart_Disease =  ("Yes" if prediction == 1 else "No")

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, data, Heart_Disease)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass

    return {
        "Heart_Disease": Heart_Disease,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
