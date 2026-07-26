from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
       step=data.step,
       amount=data.amount,
       oldbalanceOrg=data.oldbalanceOrg,
       newbalanceOrig=data.newbalanceOrig,
       oldbalanceDest=data.oldbalanceDest,
       newbalanceDest=data.oldbalanceDest,
       status_type=data.status_type,
       Is_fraud=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
