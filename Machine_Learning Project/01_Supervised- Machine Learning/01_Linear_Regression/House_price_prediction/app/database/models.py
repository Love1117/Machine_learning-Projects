from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Bedrooms = Column(Integer)
    Bathrooms = Column(Integer)
    Living_Space = Column(Integer)
    Median_Household_Income = Column(Float)
    Zip_Code = Column(Float)
    Latitude = Column(Float)
    Longitude = Column(Float)
    Address_And_City = Column(String)
    State  = Column(String)
    County  = Column(String)
    house_prediction = Column(Float)
