from app.database.models import Prediction
    
def save_prediction(db, data, Car_Price):  
    db_obj = Prediction(
        car_ModelAndYear=data.car_ModelAndYear,
        car_name=data.car_name,
        year=data.year,
        km_driven=data.km_driven,
        transmission=1 if data.transmission == "Automatic" else 0,
        mileage=data.mileage,
        engine=data.engine,
        max_power=data.max_power,
        seats=data.seats,
        fuel=data.fuel,
        owner=data.owner,
        seller_type=data.seller_type,
        Car_Price=Car_Price
    )
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
