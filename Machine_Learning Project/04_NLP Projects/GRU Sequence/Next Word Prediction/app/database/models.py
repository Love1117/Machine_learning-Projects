from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  input_word = Column(String)
  len_of_words = Column(String)
  generated_text = Column(String)
