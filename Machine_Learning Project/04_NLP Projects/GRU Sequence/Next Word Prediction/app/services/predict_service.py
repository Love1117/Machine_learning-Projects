from fastapi import HTTPException

from app.services.model_loader import model, tokenizer
from app.services.preprocessing import predict_next_words
from app.database.crud import save_prediction

  
def prediction(request, db):
  try:
    generated_text = predict_next_words(
            input_word=request.input_word,
            len_of_words=request.len_of_words,
            tokenizer=tokenizer,
            model=model
        )

    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, request, generated_text)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass


    return {
        "generated_text": generated_text,
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    print(f"Prediction error: {e}")
    import traceback
    traceback_str = traceback.format_exc()
    return {"error": f"An internal error occurred during prediction", "traceback": traceback_str, "generated_text": ""}
