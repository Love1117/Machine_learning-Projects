import numpy as np
import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.core.constants import Gender, SMOKER
from app.database.crud import save_prediction

  
def prediction(data, db):
  try:
    input_data = pd.DataFrame([{"age": data.age,
                              "sex": Gender[data.sex],
                                "bmi": data.bmi,
                                "children": data.children,
                              "smoker": SMOKER[data.smoker],
                                "region": data.region,
                                "charges": data.charges,}])

    scaled_input_data = scale.transform(input_data)

    prediction_probability = model.predict(scaled_input_data)[0][0]
    prediction_class = int(np.round(prediction_proba))


    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, data, prediction_probability, predicted_insurance_claim)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass
          

    return {
        "prediction_probability": float(prediction_probability),
        "predicted_insurance_claim": "Has Insurance" if prediction_class ==1 else "No Insurance",
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
