from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Bedrooms = Column(int)
    Bathrooms = Column(int)
    Living_Space = Column(int)
    Median_Household_Income = Column(float)
    Zip_Code = Column(float)
    Latitude = Column(float)
    Longitude = Column(float)
    Address_And_City = Column(string)
    State  = Column(string)
    County  = Column(string)
    house_prediction = Column(Float)
