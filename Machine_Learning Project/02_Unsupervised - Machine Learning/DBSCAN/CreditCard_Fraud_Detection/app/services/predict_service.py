import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_type
from app.database.crud import save_prediction


def prediction(data, db):
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
    
    if prediction==-1:
      is_fraud = "Yes"

    else:
      is_fraud = "No"
        

    db_obj = save_prediction(db, data, is_fraud)

    return {
        "prediction": is_fraud,
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
