from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Age = Column(Integer)
    Gender = Column(String)
    Education_Level = Column(Integer)
    Years_of_Experience = Column(Float)
    Country = Column(String)
    Race = Column(String)
    Senior = Column(Integer)
    Job_title = Column(String)
    predicted_salary = Column(Float)
