import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale
from app.services.preprocessing import encode_Season, encode_Appliance_Type
from app.core.constants import WEEKEND
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    Appliance_Type_encode = encode_Appliance_Type(data.Appliance_Type_status)
    Season_encode = encode_Season(data.Season_status)


    input_data = pd.DataFrame([{"Home_ID": data.Home_ID,
                                "Outdoor_Temperature_(°C)": data.Outdoor_Temperature_C, # Corrected key and reference
                                "Household_Size": data.Household_Size,
                                "Year": data.Year,
                                "Month": data.Month,
                                "Day": data.Day,
                                "Days_Of_The_Week": data.Days_Of_The_Week,
                                "Hour": data.Hour,
                                "Weekend": WEEKEND[data.Weekend],
                                **Appliance_Type_encode,
                                **Season_encode}])


    scaled_df = scale.transform(input_data)


    prediction = model.predict(scaled_df)[0][0]


    db_obj = save_prediction(db, data, prediction)

    return {
        "Energy_Consumption_(kWh)": f"{prediction:.2f}",
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
