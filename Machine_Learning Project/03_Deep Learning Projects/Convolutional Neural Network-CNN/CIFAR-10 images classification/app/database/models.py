from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "cifar_image_prediction_table"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    predicted_class_name = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
