from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  gender = Column(String)
  SeniorCitizen = Column(String)
  Partner = Column(String)
  Dependents = Column(string)
  tenure = Column(Integer)
  PhoneService = Column(String)
  MultipleLines = Column(String)
  OnlineSecurity = Column(String)
  OnlineBackup = Column(String)
  DeviceProtection = Column(String)
  TechSupport = Column(String)
  StreamingTV = Column(String)
  StreamingMovies = Column(String)
  PaperlessBilling = Column(String)
  MonthlyCharges = Column(Float)
  TotalCharges = Column(Float)
  PaymentMethod_status = Column(String)
  Contract_status = Column(String)
  InternetService_status = Column(String)
  prediction = Column(String)
  probability = Column(Float)
