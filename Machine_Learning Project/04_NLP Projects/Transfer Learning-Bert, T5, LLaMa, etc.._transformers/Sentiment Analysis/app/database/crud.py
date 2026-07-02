from app.database.models import Prediction

def save_prediction(db, model, request, sentiment_scores):
  db_obj = Prediction(
        text=request.text,
        model=model,
        sentiment_scores=sentiment_scores )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj

