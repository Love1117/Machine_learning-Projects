import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_Profession. encode_Variable
from app.core.constants import GENDER, EVER_MARRIED, GRADUATED
from app.database.crud import save_prediction

def prediction(data, db):
  bp_Profession = encode_Profession(data.Profession_status)
  bp_Variable = encode_Variable(data.Variable_status)
  
  input_data = pd.DataFrame([{"Gender": GENDER[data.Gender],
                                "Ever_Married": EVER_MARRIED[data.Ever_Married],
                                "Age": data.Age,
                                "Graduated": GRADUATED[data.Graduated],
                                "Work_Experience": data.Work_Experience,
                                "Spending_Score": data.Spending_Score,
                                "Family_Size": data.Family_Size,
                                **bp_Profession,
                                **bp_Variable}])
  
  scaled_df = scale.transform(input_data)

  prediction = model.predict(scaled_df)[0]
  
  group_mapping = {
        0: "High-Value Loyal Customers",
        1: "Budget-Conscious Shoppers",
        2: "Premium Customers",
        3: "Low Engagement Customers",
        4: "Occasional Spenders",
        5: "Occasional Spenders",
        6: "Impulse / Trend Buyers"
    }

    db_obj = save_prediction(db, data, prediction)

    return {
        "Group_into": group_mapping.get(prediction, "Unknown Group"),
        "db_id": db_obj.id
    }
