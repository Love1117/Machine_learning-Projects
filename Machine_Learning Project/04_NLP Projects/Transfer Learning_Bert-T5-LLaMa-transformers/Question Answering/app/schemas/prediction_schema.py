from pydantic import BaseModel
from typing import Literal

class Question(BaseModel):
  question: str
