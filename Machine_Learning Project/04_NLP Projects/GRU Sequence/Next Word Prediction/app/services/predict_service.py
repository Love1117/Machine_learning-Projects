import numpy as np
from fastapi import HTTPException

from app.services.model_loader import model, tokenizer
from app.services.preprocessing.py import predict_next_words
from app.database.crud import save_prediction

  
def prediction(request, db):
  try:
    generated_text = predict_next_words(
            input_word=request.input_word,
            len_of_words=request.len_of_words,
            tokenizer=tokenizer,
            model=model
        )

    db_obj = save_prediction(db, request, prediction)

    return {
        "generated_text": generated_text,
        "db_id": db_obj.id
    }
  except Exception as e:
    print(f"Prediction error: {e}")
    import traceback
    traceback_str = traceback.format_exc()
    return {"error": f"An internal error occurred during prediction: {e}", "traceback": traceback_str, "generated_text": ""}
