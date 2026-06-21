from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import JSON


Base = declarative_base()


class Prediction(Base):
  __tablename__ = "similar_word_predictions"

  id = Column(Integer, primary_key=True, index=True)
  word = Column(String)
  topn = Column(Integer)
  similar_words = Column(JSON)



class Prediction2(Base):
  __tablename__ = "word_similarity_predictions"

  id = Column(Integer, primary_key=True, index=True)
  word1 = Column(String)
  word2 = Column(String)
  similarity_score = Column(Float)
