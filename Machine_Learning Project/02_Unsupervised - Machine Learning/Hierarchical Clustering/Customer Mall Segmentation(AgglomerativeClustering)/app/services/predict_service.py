import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.core.constants import GENDER
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    input_data = pd.DataFrame([{"Gender": GENDER[data.Gender],
                                "Age": data.Age,
                                "Annual Income (k$)": data.Annual_Income_k,
                                "Spending Score (1-100)": data.Spending_Score_1_100}])

    scaled_df = scale.transform(input_data)

    prediction = model.predict(scaled_df)[0]

    if prediction==-0:
      Falls_into = "Falls_into: High-income, Low-spending customers"

    elif prediction==1:
      Falls_into = "Falls_into: Average-income, Moderate-spending customers"

    elif prediction==2:
      Falls_into = "Falls_into: High-income, High-spending customers"

    elif prediction==3:
      Falls_into = "Falls_into: Low-income, High-spending customers"
      
    else:
      Falls_into = "Falls_into: Low-income, Low-spending customers"

    db_obj = save_prediction(db, data, Falls_into)
    
    return {
        "prediction": Falls_into,
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
