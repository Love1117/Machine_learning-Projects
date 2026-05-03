from app.database.models import Prediction
from app.core.constants import GRADUATED, EVER_MARRIED, GENDER 
def save_prediction(db, data, prediction):

    db_obj = Prediction(
       Gender": GENDER[data.Gender],
       Ever_Married=EVER_MARRIED[data.Ever_Married],
       Age=data.Age,
       Graduated=GRADUATED[data.Graduated],
       Work_Experience=data.Work_Experience,
       Spending_Score=data.Spending_Score,
       Family_Size=data.Family_Size,
       Profession_status=data.Family_Size,
       Variable_status=data.Variable_status,
       Group_into=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
