from app.database.models import Prediction

def save_prediction(db, data, is_fraud):

    db_obj = Prediction(
       step=data.step,
       amount=data.amount,
       oldbalanceOrg=data.oldbalanceOrg,
       newbalanceOrig=data.newbalanceOrig,
       oldbalanceDest=data.oldbalanceDest,
       newbalanceDest=data.oldbalanceDest,
       type_status=data.type_status,
       Is_fraud=is_fraud
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
