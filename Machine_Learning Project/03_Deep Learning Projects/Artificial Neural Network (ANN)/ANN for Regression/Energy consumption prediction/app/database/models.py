from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
  

class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  Home_ID = Column(Integer)
  Outdoor_Temperature_C = Column(Float)
  Household_Size = Column(Float)
  Year = Column(Integer)
  Month = Column(Integer)
  Day = Column(Integer)
  Days_Of_The_Week = Column(Integer)
  Hour = Column(Float)
  Weekend = Column(String)
  Appliance_Type_status = Column(String)
  Season_status = Column(String)
  prediction = Column(Float)
