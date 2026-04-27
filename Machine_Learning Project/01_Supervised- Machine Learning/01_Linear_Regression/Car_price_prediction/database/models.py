from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Prediction(Base):
    __tablename__ = "predictions"
  
    id = Column(Integer, primary_key=True, index=True)
    car_ModelAndYear = column(string)
    car_name = column(string)
    year = column(int)
    km_driven = column(float)
    transmission = column(float)
    mileage = column(float)
    engine = column(float)
    max_power = column(float)
    seats = column(float)
    fuel = column(string)
    owner = column(string)
    seller_type = column(string)
