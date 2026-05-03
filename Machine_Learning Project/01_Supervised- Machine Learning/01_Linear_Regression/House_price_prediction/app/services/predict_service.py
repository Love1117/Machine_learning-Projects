import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale, AddressAndCity_Encoder, State_Encoder, County_Encoder
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    if data.Address_And_City not in AddressAndCity_Encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Address_And_City",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(AddressAndCity_Encoder.keys())[:5]
            }
        )

    if data.State not in State_Encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid State",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(State_Encoder.keys())[:5]
            }
        )

    if data.County not in County_Encoder:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid County",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(County_Encoder.keys())[:5]
            }
        )

    

    AddressAndCity_Encoded = AddressAndCity_Encoder[data.Address_And_City]
    State_Encoded = State_Encoder[data.State]
    County_Encoded = County_Encoder[data.County]




    
    input_data = pd.DataFrame([{"Bedrooms": data.Bedrooms,
                              "Bathrooms": data.Bathrooms,
                              "Living_Space": data.Living_Space,
                              "Median_Household_Income": data.Median_Household_Income,
                              "Zip_Code": data.Zip_Code,
                              "Latitude": data.Latitude,
                              "Longitude": data.Longitude,
                              "Address_And_City": AddressAndCity_Encoded,
                              "State": State_Encoded,
                              "County": County_Encoded}])
    
    input_data = input_data[["Bedrooms",
                             "Bathrooms",
                             "Living_Space",
                             "Median_Household_Income",
                             "Zip_Code",
                             "Latitude",
                             "Longitude",
                             "Address_And_City",
                             "State",
                             "County"]]

    scaled_df = scale.transform(input_data)

    prediction = float(round(model.predict(scaled_df)[0], 2))

    db_obj = save_prediction(db, data, prediction)

    return {
        "House_price": prediction,
        "db_id": db_obj.id
    }
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
