from sqlalchemy.orm import Session
from app.database.models import Prediction

def save_prediction(db: Session, filename: str, predicted_digit: int):
    db_obj = Prediction(
        filename=filename,
        predicted_digit=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
