from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
  __tablename__ = "predictions"

  id = Column(Integer, primary_key=True, index=True)
  gender = Column(string)
  SeniorCitizen = Column(string)
  Partner = Column(string)
  Dependents = Column(string)
  tenure = Column(int)
  PhoneService = Column(string)
  MultipleLines = Column(string)
  OnlineSecurity = Column(string)
  OnlineBackup = Column(string)
  DeviceProtection = Column(string)
  TechSupport = Column(string)
  StreamingTV = Column(string)
  StreamingMovies = Column(string)
  PaperlessBilling = Column(string)
  MonthlyCharges = Column(Float)
  TotalCharges = Column(Float)
  PaymentMethod_status = Column(string)
  Contract_status = Column(string)
  InternetService_status = Column(string)
  prediction = Column(Float)
