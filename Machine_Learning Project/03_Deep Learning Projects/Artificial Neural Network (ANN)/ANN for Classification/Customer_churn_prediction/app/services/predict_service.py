import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scaler, car_model_encoder, car_name_encoder
from app.services.preprocessing import encode_fuel, encode_owner, encode_seller_type
from app.core.constants import Fuel_Columns, Owner_Columns, Seller_type_Columns, Transmission_Map
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    PaymentMethod_encode = encode_PaymentMethod(data.PaymentMethod_status)
    Contract_encode = encode_Contract(data.Contract_status)
    InternetService_encode = encode_InternetService(data.InternetService_status)

    input_data = pd.DataFrame([{"gender": GENDER[data.gender],
                                "SeniorCitizen": Senior_Citizen[data.SeniorCitizen],
                                "Partner": PARTNER[data.Partner],
                                "Dependents": DEPENDENT[data.Dependents],
                                "tenure": data.tenure,
                                "PhoneService": Phone_Sevice[data.PhoneService],
                                "MultipleLines": Multi_Lines[data.MultipleLines],
                                "OnlineSecurity": Online_Security[data.OnlineSecurity],
                                "OnlineBackup": Online_Backup[data.OnlineBackup],
                                "DeviceProtection": Device_Protection[data.DeviceProtection],
                                "TechSupport": Tech_Support[data.TechSupport],
                                "StreamingTV": Streaming_TV[data.StreamingTV],
                                "StreamingMovies": Streaming_Movies[data.StreamingMovies],
                                "PaperlessBilling": Peperless_Billings[data.PaperlessBilling],
                                "MonthlyCharges": data.MonthlyCharges,
                                "TotalCharges": data.TotalCharges,
                                **PaymentMethod_encode,
                                **Contract_encode,
                                **InternetService_encode}])

    large = ["tenure","MonthlyCharges","TotalCharges"]

    input_data[large] = scale.transform(input_data[large])

    scaled_df = input_data

    probability = model.predict(scaled_df)[0][0]
    prediction_class = 1 if probability >= 0.5 else 0


    db_obj = save_prediction(db, data, prediction_class, probability)

    return {
        "prediction_probability": float(probability),
        "Prediction": "Customer Left" if prediction_class == 1 else "Customer Retained",
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
