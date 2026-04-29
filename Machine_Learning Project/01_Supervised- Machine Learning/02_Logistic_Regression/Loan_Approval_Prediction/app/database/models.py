from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    Age  = Column(int)
    Gender = Column(String)
    Education = Column(String)
    Income = Column(Float)
    Employment_experience  = Column(Float)
    Home_ownership = Column(string)
    Loan_amount = Column(Float)
    Loan_intent = Column(String)
    Loan_interest_rate = Column(Float)
    Loan_percent_income = Column(Float)
    Credit_history_length = Column(Float)
    Credit_score = Column(Float)
    Previous_loan_defaults_on_file = Column(String)
    Outcome_status = Column(string)
