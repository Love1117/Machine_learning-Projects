import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import tfidf_vectorizer, model
from app.database.crud import save_prediction


def prediction(text_input, db):
  try:
    new_vec = tfidf_vectorizer.transform([text_input.text])

    prediction = model.predict(new_vec)

    result = "Spam" if prediction[0] == 1 else "Not-Spam"


    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, text_input,  prediction)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass
          

    return {
        "input_text": text_input.text, 
        "prediction": result,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
