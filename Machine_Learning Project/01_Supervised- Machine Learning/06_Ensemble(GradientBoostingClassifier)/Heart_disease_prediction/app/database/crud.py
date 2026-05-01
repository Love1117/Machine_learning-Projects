from app.core.constants import SMOKE, ALCOHOL, PHYSICAL, GENDER
from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
        car_ModelAndYear=data.car_ModelAndYear,
        car_name=data.car_name,
        year=data.year,
        km_driven=data.km_driven,
        transmission=1 if data.transmission == "Automatic" else 0,
        mileage=data.mileage,
        engine=data.engine,
        max_power=data.max_power,
        seats=data.seats,
        fuel=data.fuel,
        owner=data.owner,
        seller_type=data.seller_type,
        prediction=prediction

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
      Heart_Disease=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
