from pydantic import BaseModel, Field

class SimilarWordsRequest(BaseModel):
    word: str
    topn: int = 10  

class WordSimilarityRequest(BaseModel):
    word1: str
    word2: str
