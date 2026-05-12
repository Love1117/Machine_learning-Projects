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

    db_obj = save_prediction(db, request, "similar_words": result)

    return {request,
            "similar_words": result,
            "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")





def next_prediction(request, db):
  try:
    for word in [request.word1, request.word2]:
      if word not in word2vec_model.wv.key_to_index:
        raise HTTPException(
                    status_code=404,
                    detail=f"Word '{word}' not found in the model's vocabulary. Please ensure both words exist."
                )
    similarity = word2vec_model.wv.similarity(request.word1, request.word2)
    
    db_obj_one = save_prediction2(db, request, similarity)

    return {request,
            "similarity": float(similarity),
            "db_id": db_obj_one.id
    }

  except Exception as e:
    raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
