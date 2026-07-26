from app.database.models import Prediction

def save_prediction(db, data, prediction):

    db_obj = Prediction(
        Bedrooms = data.Bedrooms,
        Bathrooms = data.Bathrooms,
        Living_Space = data.Living_Space,
        Median_Household_Income = data.Median_Household_Income,
        Zip_Code = data.Zip_Code,
        Latitude = data.Latitude,
        Longitude = data.Longitude,
        Address_And_City = data.Address_And_City,
        State = data.State,
        County = data.County,
        House_price = prediction)

  
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
