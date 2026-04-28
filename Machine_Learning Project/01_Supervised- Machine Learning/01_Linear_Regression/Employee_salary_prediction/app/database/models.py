from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Age = Column(int)
    Gender = Column(string)
    Education_Level = Column(int)
    Years_of_Experience = Column(Float)
    Country = Column(string)
    Race = Column(string)
    Senior = Column(int)
    Job_title = Column(string)
    predicted_salary = Column(Float)
