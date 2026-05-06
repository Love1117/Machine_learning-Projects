from app.database.models import Prediction


def save_prediction(db, request, generated_text):
  db_obj = Prediction(
        input_word=request.input_word,
        len_of_words=request.len_of_words,
        generated_text=generated_text
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
