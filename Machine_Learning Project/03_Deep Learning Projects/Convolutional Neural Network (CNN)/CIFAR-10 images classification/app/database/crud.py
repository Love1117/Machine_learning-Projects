from sqlalchemy.orm import Session
from app.database.models import Prediction

def save_prediction(db: Session, filename, predicted_class_name, confidence):
    db_obj = Prediction(
        filename=filename,  
        predicted_class_name=predicted_class_name,
        confidence=confidence)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
