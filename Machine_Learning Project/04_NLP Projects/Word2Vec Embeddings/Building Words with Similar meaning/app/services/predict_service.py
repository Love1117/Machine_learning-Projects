from fastapi import HTTPException

from app.services.model_loader import word2vec_model
from app.database.crud import save_prediction, save_prediction2


def prediction(request, db):
  try:
    if request.word not in word2vec_model.wv.key_to_index:
            raise HTTPException(
                status_code=404,
                detail=f"Word '{request.word}' not found in the model's vocabulary. Try a different word."
            )
        
    similar_words = word2vec_model.wv.most_similar(request.word, topn=request.topn)
    result = [{
            "word": word,
            "similarity": float(score) # Convert numpy float to standard float
        } for word, score in similar_words]


    db_id = None
    database_saved = False
    
    try:
        db_obj = save_prediction(db, request, result)
        db_id = db_obj.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass

    return {
    "word": request.word,
    "topn": request.topn,
    "similar_words": result,
    "db_id": db_id,
    "database_saved": database_saved}


  except HTTPException:
    raise
  
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")





def next_prediction(request, db):
  try:
    for word in [request.word1, request.word2]:
      if word not in word2vec_model.wv.key_to_index:
        raise HTTPException(
                    status_code=404,
                    detail=f"Word '{word}' not found in the model's vocabulary. Please ensure both words exist."
                )
    similarity = word2vec_model.wv.similarity(request.word1, request.word2)


    db_id = None
    database_saved = False
    
    try:
        db_obj_one = save_prediction(db, request, similarity)
        db_id = db_obj_one.id
        database_saved = True
     
    except Exception as db_error:
        traceback.print_exc()
        try:
            db.rollback()
        except Exception:
            pass

    return {
    "word1": request.word1,
    "word2": request.word2,
    "similarity": float(similarity),
    "db_id": db_id,
    "database_saved": database_saved}

  except HTTPException:
    raise
    
  except Exception as e:
    raise HTTPException(status_code=500, detail="An error occurred while processing the prediction.")
