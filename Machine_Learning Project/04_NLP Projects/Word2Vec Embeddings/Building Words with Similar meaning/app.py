from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import gensim
import os
from pathlib import Path




# loading model from the path where the Word2Vec model is saved

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models" / "1st_version"

word2vec_model = gensim.models.Word2Vec.load(MODEL_DIR / "CreditCard_fraud_transaction.joblib")


# Initialize the FastAPI application
app = FastAPI(
    title="Word Similarity API for Netflix Reviews",
    description="A simple API using a Gensim Word2Vec model to find similar words and calculate word similarity from Netflix review data."
)



class SimilarWordsRequest(BaseModel):
    word: str
    topn: int = 10  # Default to 10 similar words if not specified

class WordSimilarityRequest(BaseModel):
    word1: str
    word2: str

# --- API Endpoints ---

@app.get("/health")
async def health_check():
    """Checks if the API is running and the model is loaded."""
    if word2vec_model:
        return {"status": "healthy", "model_loaded": True}
    else:
        # This case should ideally not happen if startup_event raises an error on failure.
        raise HTTPException(status_code=500, detail="Model not loaded yet or failed to load.")

@app.post("/similar_words")
async def get_similar_words(request: SimilarWordsRequest):
    """Returns words most similar to the given word."""
    try:
        # Check if the word exists in the model's vocabulary
        if request.word not in word2vec_model.wv.key_to_index:
            raise HTTPException(
                status_code=404,
                detail=f"Word '{request.word}' not found in the model's vocabulary. Try a different word."
            )
        
        similar_words = word2vec_model.wv.most_similar(request.word, topn=request.topn)
        # Format the output for better readability
        result = [{
            "word": word,
            "similarity": float(score) # Convert numpy float to standard float
        } for word, score in similar_words]
        return {"query_word": request.word, "similar_words": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/word_similarity")
async def get_word_similarity(request: WordSimilarityRequest):
    """Calculates the similarity between two given words."""    
    try:
        # Check if both words exist in the model's vocabulary
        for word in [request.word1, request.word2]:
            if word not in word2vec_model.wv.key_to_index:
                raise HTTPException(
                    status_code=404,
                    detail=f"Word '{word}' not found in the model's vocabulary. Please ensure both words exist."
                )

        similarity = word2vec_model.wv.similarity(request.word1, request.word2)
        return {
            "word1": request.word1,
            "word2": request.word2,
            "similarity": float(similarity) # Convert numpy float to standard float
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
