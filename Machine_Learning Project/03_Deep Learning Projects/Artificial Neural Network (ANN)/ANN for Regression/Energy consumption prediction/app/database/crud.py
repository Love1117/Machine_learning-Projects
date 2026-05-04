from app.database.models import Prediction
from app.core.constants import WEEKEND

def save_prediction(db, data, prediction):
  db_obj = Prediction(
        Home_ID=data.Home_ID,
        Outdoor_Temperature_C=data.Outdoor_Temperature_C, # Corrected key and reference
        Household_Size=data.Household_Size,
        Year=data.Year,
        Month=data.Month,
        Day=data.Day,
        Days_Of_The_Week=data.Days_Of_The_Week,
        Hour=data.Hour,
        Weekend=WEEKEND[data.Weekend],
        Appliance_Type_status=data.Appliance_Type_status,
        Season_status=data.Season_status  
        Energy_Consumption_kWh=prediction
       )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
