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

    db_obj = save_prediction(db, question_data, context, answer, score)

    return {
        "question": question,
        "context": context,
        "answer": result["answer"],
        "score": result["score"],
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
