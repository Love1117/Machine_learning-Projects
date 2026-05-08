from app.database.models import Prediction


def save_prediction(db, text_input, result):
  db_obj = Prediction(
        text=text_input.text,
        prediction=result
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
