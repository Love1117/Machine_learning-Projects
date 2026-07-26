from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
    limit_phrases: int
    limit_sentences: int
