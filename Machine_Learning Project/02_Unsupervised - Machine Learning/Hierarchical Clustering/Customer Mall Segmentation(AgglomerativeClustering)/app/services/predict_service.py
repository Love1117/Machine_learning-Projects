import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.core.constants import GENDER
from app.database.crud import save_prediction


def prediction(data, db):
  input_data = pd.DataFrame([{"Gender": GENDER[data.Gender],
                                "Age": data.Age,
                                "Annual Income (k$)": data.Annual_Income_k,
                                "Spending Score (1-100)": data.Spending_Score_1_100}])

  scaled_df = scale.transform(input_data)

  prediction = model.predict(scaled_df)[0]

  group_mapping = {
        0:"High-income, Low-spending customers",
        1:"Average-income, Moderate-spending customers",
        2: "High-income, High-spending customers",
        3: "Low-income, High-spending customers",
        4: "Low-income, Low-spending customers"}


  db_obj = save_prediction(db, data, prediction)

  return {
        "Falls_Into": group_mapping.get(prediction, "Unknown Group",
        "db_id": db_obj.id
    }
