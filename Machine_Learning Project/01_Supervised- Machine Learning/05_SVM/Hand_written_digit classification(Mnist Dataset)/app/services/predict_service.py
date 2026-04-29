import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model
from app.database.crud import save_prediction


def prediction(data, db):

    
    input_dict = {
        "car_ModelAndYear": car_model_val,
        "car_name": car_name_val,
        "year": data.year,
        "km_driven": data.km_driven,
        "transmission": Transmission_Map[data.transmission],
        "mileage": data.mileage,
        "engine": data.engine,
        "max_power": data.max_power,
        "seats": data.seats,
        **fuel_encoded,
        **owner_encoded,
        **seller_encoded
    }

    columns = [
        "car_ModelAndYear",
        "car_name",
        "year",
        "km_driven",
        "transmission",
        "mileage",
        "engine",
        "max_power",
        "seats",
    ] + Fuel_Columns + Owner_Columns + Seller_type_Columns

    df = pd.DataFrame([input_dict]).reindex(columns=columns, fill_value=0)

    scaled = scaler.transform(df)
    prediction = float(round(model.predict(scaled)[0], 2))

    db_obj = save_prediction(db, data, prediction)

    return {
        "car_price": prediction,
        "db_id": db_obj.id
    }
