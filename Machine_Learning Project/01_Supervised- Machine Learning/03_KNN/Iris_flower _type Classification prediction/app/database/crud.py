from app.database.models import Prediction

def save_prediction(db, data, iris_flower):

    db_obj = Prediction(
        sepal_length=data.sepal_length,
        sepal_width=data.sepal_width,
        petal_length=data.petal_length,
        petal_width=data.petal_width,
        prediction=iris_flower)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
