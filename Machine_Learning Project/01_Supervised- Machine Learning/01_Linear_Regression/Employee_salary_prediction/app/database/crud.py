from app.database.models import Prediction
from app.core.constants import Gend, Senio
def save_prediction(db, data, prediction):

    db_obj = Prediction(
        Age = data.Age,
        Gender = Gend[data.Gender],
        Education_Level = data.Education_Level,
        Years_of_Experience = data.Years_of_Experience,
        Country = data.Country,
        Race = data.Race,
        Senior = Senio[data.Senior],
        Job_title = data.Job_title,
        employee_salary = prediction)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
