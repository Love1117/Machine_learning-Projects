from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Gender = Column(String)
    Ever_Married = Column(String)
    Age = Column(Strig)
    Graduated = Column(String)
    Work_Experience = Column(Float)
    Spending_Score = Column(Integer)
    Family_Size = Column(Float)
    Profession_status = Column(String)
    Variable_status = Column(String)
    prediction = Column(String)
