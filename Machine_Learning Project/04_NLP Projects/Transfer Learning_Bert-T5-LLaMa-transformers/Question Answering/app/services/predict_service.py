from fastapi import HTTPException

from app.services.model_loader import qa_pipeline
from app.database.crud import save_prediction
from app.core.constants import qa_data



def prediction(question_data, db):
  try:
    if qa_pipeline is None:
        return {"error": "Model not loaded"}

    question = question_data.question

    # Auto-pick context
    context = qa_data.get(question)

    if context is None:
        return {"error": "Question not found in database"}

    result = qa_pipeline(question=question, context=context)
    
    answer = result["answer"]
    score = result["score"]


    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, question_data, context, answer, score)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass
    

    return {
        "question": question,
        "context": context,
        "answer": result["answer"],
        "score": result["score"],
        "db_id": db_id,
        "database_saved": database_saved
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
