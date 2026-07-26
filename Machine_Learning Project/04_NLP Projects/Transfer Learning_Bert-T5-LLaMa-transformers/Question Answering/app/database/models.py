from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "question_anwsering_table"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    context = Column(String)
    answer = Column(String)
    score = Column(Float)
