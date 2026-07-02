from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    systolic_blood_pressure = Column(Integer)
    diastolic_blood_pressure = Column(Integer)
    cholesterol = Column(Integer)
    gluc = Column(Integer)
    smoke= Column(String)
    alcohol_intake= Column(String)
    Physical_activity= Column(String)
    age = Column(Integer)
    bmi = Column(Float)
    bp_status = Column(String)
    prediction = Column(String)
