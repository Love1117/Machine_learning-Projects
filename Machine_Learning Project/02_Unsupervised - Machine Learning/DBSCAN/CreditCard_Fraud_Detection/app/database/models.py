from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "credit_card_fraud_table"

    id = Column(Integer, primary_key=True, index=True)
    step = Column(Float)
    amount = Column(Float)
    oldbalanceOrg = Column(Float)
    newbalanceOrig = Column(Float)
    oldbalanceDest = Column(Float)
    newbalanceDest = Column(Float)
    status_type = Column(String)
    Is_fraud = Column(String)
