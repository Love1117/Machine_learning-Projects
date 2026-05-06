from app.database.models import Prediction
from app.core.constants import SMOKER, Gender


def save_prediction(db, data, prediction_class, prediction_probability):
  db_obj = Prediction(
        age=data.age,
        sex=Gender[data.sex],
        bmi=data.bmi,
        children=data.children,
        smoker=SMOKER[data.smoker],
        region=data.region,
        charges=data.charges
        prediction_class=prediction_class,
        prediction_probability=prediction_probability
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
