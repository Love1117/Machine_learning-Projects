from app.core.constants import SMOKE, ALCOHOL, PHYSICAL, GENDER
from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
      gender=GENDER[data.gender],
      height=data.height,
      weight=data.weight,
      systolic_blood_pressure=data.systolic_blood_pressure,
      diastolic_blood_pressure=data.diastolic_blood_pressure,
      cholesterol=data.cholesterol, # Corrected typo here
      gluc=data.gluc,
      salcohol_intake=ALCOHOL[data.alcohol_intake],
      Physical_activity=PHYSICAL[data.Physical_activity],
      age=data.age,
      bmi=data.bmi,
      bp_status=data.bp_status,
      prediction=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
