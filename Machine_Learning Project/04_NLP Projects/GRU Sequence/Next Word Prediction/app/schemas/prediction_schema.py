from pydantic import BaseModel, Field
from typing import Literal

class PredictionRequest(BaseModel):
  input_word: str
  len_of_words: int
