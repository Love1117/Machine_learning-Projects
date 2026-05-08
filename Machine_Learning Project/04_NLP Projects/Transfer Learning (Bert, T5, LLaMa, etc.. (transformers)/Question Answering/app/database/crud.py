from app.database.models import Prediction

def save_prediction(db, question_data, context, answer, score):
    db_obj = Prediction(
    question=question_data.question
    context=context
    answer=answer
    score=score)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
