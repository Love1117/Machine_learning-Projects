from app.database.models import Prediction
from app.core.constants import GENDER
def save_prediction(db, data, prediction):

    db_obj = Prediction(
        Gender=GENDER[data.Gender],
        Age=data.Age,
        Annual_Income_k=data.Annual_Income_k,
        Spending_Score_1_100=data.Spending_Score_1_100,
        prediction=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
