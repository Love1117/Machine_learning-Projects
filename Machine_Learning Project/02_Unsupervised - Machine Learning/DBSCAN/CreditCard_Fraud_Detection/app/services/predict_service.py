import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_type
from app.database.crud import save_prediction
import traceback


def prediction(data, db):
  try:
    type_encoded = encode_type(data.status_type)

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

    prediction = is_fraud

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, data,  prediction)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass

    return {
        "Is_Fraud": is_fraud,
        "db_id": db_id,
        "database_saved": database_saved
    }
    
  except Exception as e:
    import traceback
    traceback.print_exc()

    raise HTTPException(
        status_code=500,
        detail=str(e)
    )
