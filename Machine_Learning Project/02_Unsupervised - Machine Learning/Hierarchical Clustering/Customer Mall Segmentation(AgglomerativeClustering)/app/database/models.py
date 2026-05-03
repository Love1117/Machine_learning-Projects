from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Gender = Column(string)
    Age = Column(int)
    Annual_Income_k = Column(Float)
    Spending_Score_1_100 = Column(Float)
    prediction = Column(string)
