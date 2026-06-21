from app.database.models import Prediction


def save_prediction(db, text_input, prediction):
  db_obj = Prediction(
        text=text_input.text,
        prediction=prediction
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
