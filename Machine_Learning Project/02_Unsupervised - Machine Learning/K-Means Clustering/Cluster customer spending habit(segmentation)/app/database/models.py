from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Gender = Column(string)
    Ever_Married = Column(string)
    Age = Column(strig)
    Graduated = Column(string)
    Work_Experience = Column(Float)
    Spending_Score = Column(int)
    Family_Size = Column(Float)
    Profession_status = Column(string)
    Variable_status = Column(string)
    prediction = Column(string)
