from fastapi import APIRouter, HTTPExceptiopn, Depends
from sqlalchemy.orm import Session

from app.schemas.prediction_schema import SimilarWordsRequest, WordSimilarityRequest
from app.services.predict_service import prediction, next_prediction
from app.services.model_loader import word2vec_model
from app.database.session import get_db



router = APIRouter()



@router.get("/health")
def health_check():
    """Checks if the API is running and the model is loaded."""
    if word2vec_model:
        return {"status": "healthy", "model_loaded": True}
    else:
        raise HTTPException(status_code=500, detail="Model not loaded yet or failed to load.")


@router.post("/similar_words")
def get_similar_words(request: SimilarWordsRequest, db: Session = Depends(get_db)):
    """Returns words most similar to the given word."""
    return prediction(request, db)



@router.post("/word_similarity")
def def get_word_similarity(request: WordSimilarityRequest, db: Session = Depends(get_db)):
    """Calculates the similarity between two given words."""
    return next_prediction(request, db)
