from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        iris_flower=prediction)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
