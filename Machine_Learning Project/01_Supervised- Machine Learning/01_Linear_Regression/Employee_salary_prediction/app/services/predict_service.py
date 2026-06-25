import pandas as pd
from fastapi import HTTPException
import traceback
from app.services.model_loader import model, scale, Country_freq, Race_freq, Job_title_encoder
from app.core.constants import Gend, Senio, EDUCATION
from app.database.crud import save_prediction


def prediction(data, db):
  try:  
    if data.Country not in Country_freq:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Country",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(Country_freq.keys())[:5]
            }
        )

    if data.Race not in Race_freq:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Race",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(Race_freq.keys())[:5]
            }
        )

    if data.Job_title not in Job_title_encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Job_title",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(Job_title_encoder.keys())[:5]
            }
        )

    

    Country_val = Country_freq(data.Country)
    Race_val = Race_freq(data.Race)
    Job_title_val = Job_title_encoder(data.Job_title)

    input_data = pd.DataFrame([{"Age": data.Age,
                                "Gender": Gend[data.Gender],
                                "Education_Level": EDUCATION[data.Education_Level],
                                "Years_of_Experience": data.Years_of_Experience,
                                "Country": Country_val,
                                "Race": Race_val,
                                "Senior": Senio[data.Senior],
                                "Job_title": Job_title_val}])
    input_data = input_data[["Age",
                             "Gender",
                             "Education_Level",
                             "Years_of_Experience",
                             "Country",
                             "Race",
                             "Senior",
                             "Job_title"]]

    Scaled = scale.transform(input_data)
    prediction = float(round(model.predict(Scaled)[0], 2))
    Employee_Salary =  f"{prediction:,.2f}"
    
    db_obj = save_prediction(db, data, Employee_Salary)

    return {
        "Employee_Salary": Employee_Salary,
        "db_id": db_obj.id
    }
    
  except Exception as e:
    traceback.print_exc()
    raise HTTPException(status_code=500, detail=str(e))
