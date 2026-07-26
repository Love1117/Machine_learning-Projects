import pytextrank
from fastapi import HTTPException

from app.services.model_loader import model
from app.database.crud import save_prediction


def prediction(input_data, db):
  try:
    doc = model(input_data.text)
    summary_sentences = []
    for sent in doc._.textrank.summary(limit_phrases=input_data.limit_phrases, limit_sentences=input_data.limit_sentences):
        summary_sentences.append(str(sent))


    db_obj = save_prediction(db, input_data, summary)

    return {
        "summary": " ".join(summary_sentences),
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
