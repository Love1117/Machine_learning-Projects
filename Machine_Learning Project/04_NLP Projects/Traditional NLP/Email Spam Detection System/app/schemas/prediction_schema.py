from pydantic import BaseModel, Field
from typing import Literal

class TextInput(BaseModel):
  text: str
