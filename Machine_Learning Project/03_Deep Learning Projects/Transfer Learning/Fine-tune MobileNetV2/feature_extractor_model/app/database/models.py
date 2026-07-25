from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "vector_image_classifier_table"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    predicted_class_name = Column(String)
    confidence = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
