from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "gru_next_word_prediction_table"

  id = Column(Integer, primary_key=True, index=True)
  input_word = Column(String)
  len_of_words = Column(Integer)
  generated_text = Column(String)
