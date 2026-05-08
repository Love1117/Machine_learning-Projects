import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import tfidf_vectorizer, model
from app.database.crud import save_prediction


def prediction(text_input, db):
  try:
    new_vec = tfidf_vectorizer.transform([text_input.text])

    prediction = model.predict(new_vec)

    result = "Spam" if prediction[0] == 1 else "Not-Spam"
    
    db_obj = save_prediction(db, text_input, result)

    return {
        "input_text": text_input.text, 
        "prediction": result,
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
