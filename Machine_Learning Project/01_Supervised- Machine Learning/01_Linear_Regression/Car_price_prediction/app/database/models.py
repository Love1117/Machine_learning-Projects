from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)

    car_ModelAndYear = Column(Float)
    car_name = Column(Float)
    year = Column(Integer)
    km_driven = Column(Float)
    transmission = Column(Integer)
    mileage = Column(Float)
    engine = Column(Float)
    max_power = Column(Float)
    seats = Column(Float)
    fuel = Column(String)
    owner = Column(String)
    seller_type = Column(String)
    car_price = Column(Float)
