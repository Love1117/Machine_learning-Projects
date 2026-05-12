from app.database.models import Prediction, Prediction2


def save_prediction(db, request, similar_words):
  db_obj = Prediction(
        word=request.word,
        topn=request.topn,
        similar_words=similar_words)

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)
  return db_obj



def save_prediction2(db, request, similarity):
  db_obj_one = Prediction2(
        word1=request.word1,
        word2=request.word2,
        similarity_score=similarity)
  db.add(db_obj_one)
  db.commit()
  db.refresh(db_obj_one)
  return db_obj_one
