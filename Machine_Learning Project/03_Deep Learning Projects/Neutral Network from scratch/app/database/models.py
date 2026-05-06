from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  age = Column(Integer)
  sex = Column(String)
  bmi = Column(Float)
  children = Column(Integer)
  smoker = Column(String)
  region = Column(Integer)
  charges = Column(Float)
  prediction_probability = Column(Float)
  prediction_class = Column(String)
