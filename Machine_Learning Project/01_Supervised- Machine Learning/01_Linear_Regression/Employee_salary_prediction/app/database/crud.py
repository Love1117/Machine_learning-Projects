from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
        Age = data.Age,
        Gender = 1 if data.Gender == "Male" else 0,
        Education_Level = data.Education_Level,
        Years_of_Experience = data.Years_of_Experience,
        Country = data.Country,
        Race = data.Race,
        Senior = data.Senior,
        Job_title = data.Job_title  
        employee_salary = predicted_salary
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
