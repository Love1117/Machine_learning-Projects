from app.database.models import Prediction
from app.core.constants import GENDER, Senior_Citizen, PARTNER, DEPENDENT, Phone_Sevice, Multi_Lines, Online_Security, Online_Backup, Device_Protection, Tech_Support, Streaming_TV, Streaming_Movies, Peperless_Billings
def save_prediction(db, data, prediction_class, probability):
  db_obj = Prediction(
        gender=GENDER[data.gender],
        SeniorCitizen=Senior_Citizen[data.SeniorCitizen],
        Partner=PARTNER[data.Partner],
        Dependents=DEPENDENT[data.Dependents],
        tenure=data.tenure,
        PhoneService=Phone_Sevice[data.PhoneService],
        MultipleLines=Multi_Lines[data.MultipleLines],
        OnlineSecurity=Online_Security[data.OnlineSecurity],
        OnlineBackup=Online_Backup[data.OnlineBackup],
        DeviceProtection=Device_Protection[data.DeviceProtection],
        TechSupport=Tech_Support[data.TechSupport],
        StreamingTV=Streaming_TV[data.StreamingTV],
        StreamingMovies=Streaming_Movies[data.StreamingMovies],
        PaperlessBilling=Peperless_Billings[data.PaperlessBilling],
        MonthlyCharges=data.MonthlyCharges,
        TotalCharges=data.TotalCharges,
        PaymentMethod_status=data.PaymentMethod_status,
        Contract_status=data.Contract_status,
        InternetService_status=data.InternetService_status,
        prediction=prediction_class,
        probability=probability
    )

  db.add(db_obj)
  db.commit()
  db.refresh(db_obj)

  return db_obj
