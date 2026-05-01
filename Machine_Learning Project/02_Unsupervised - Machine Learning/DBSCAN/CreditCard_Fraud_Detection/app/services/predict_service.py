import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_type
from app.database.crud import save_prediction


def prediction(data, db):
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


    db_obj = save_prediction(db, data, prediction)

    return {
        "is_fraud: Yes" if prediction == -1 else "is_fraud:: No",
        "db_id": db_obj.id
    }
