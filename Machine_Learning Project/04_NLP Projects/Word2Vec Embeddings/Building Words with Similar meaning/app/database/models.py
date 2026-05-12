from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions for similar_words"

  id = Column(Integer, primary_key=True, index=True)
  word = Column(String)
  topn = Column(Integer)
  similar_words = Column(String)



class Prediction2(Base):
  __tablename__ = "predictions for word_similarity"

  id = Column(Integer, primary_key=True, index=True)
  word1 = Column(String)
  word2 = Column(String)
  similarity_score = Column(Float)
