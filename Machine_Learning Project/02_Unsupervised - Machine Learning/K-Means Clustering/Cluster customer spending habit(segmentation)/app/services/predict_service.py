import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_Profession. encode_Variable
from app.core.constants import GENDER, EVER_MARRIED, GRADUATED
from app.database.crud import save_prediction


def prediction(data, db):
  try:
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
  
    if prediction==-0:
      Group_into = "High-Value Loyal Customers"

    elif prediction==1:
      Group_into = "Budget-Conscious Shoppers"

    elif prediction==2:
      Group_into = "Premium Customers"

    elif prediction==3:
      Group_into = "Low Engagement Customers"

    elif prediction==4:
      Group_into = "Occasional Spenders"

    elif prediction==5:
      Group_into = "Regular Mid-Spenders"
            
    else:
      Group_into = "Impulse / Trend Buyers"

    db_obj = save_prediction(db, data, Group_into)
    
    return {
        "prediction": Group_into,
        "db_id": db_obj.id
    }
