import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scaler, car_model_encoder, car_name_encoder
from app.services.preprocessing import encode_fuel, encode_owner, encode_seller_type
from app.core.constants import Fuel_Columns, Owner_Columns, Seller_type_Columns, Transmission_Map
from app.database.crud import save_prediction


def prediction(data, db):

    if data.car_ModelAndYear not in car_model_encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid car_ModelAndYear",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(car_model_encoder.keys())[:5]
            }
        )

    if data.car_name not in car_name_encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid car_name",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(car_name_encoder.keys())[:5]
            }
        )

    fuel_encoded = encode_fuel(data.fuel)
    owner_encoded = encode_owner(data.owner)
    seller_encoded = encode_seller_type(data.seller_type)

    car_model_val = car_model_encoder[data.car_ModelAndYear]
    car_name_val = car_name_encoder[data.car_name]

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
