from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  text = Column(String)
  prediction = Column(String)
