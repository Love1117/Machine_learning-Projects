from app.database.models import Prediction

def save_prediction(db, input_data, summary):
    db_obj = Prediction(
    text=input_data.text,
    limit_phrases=input_data.limit_phrases,
    limit_sentences=input_data.limit_sentences,
    summary=summary)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
