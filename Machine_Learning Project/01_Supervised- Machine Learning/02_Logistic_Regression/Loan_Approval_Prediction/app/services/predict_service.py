import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model, scale, Loan_intent_freq, Home_ownership_freq
from app.core.constants import GENDER, EDUCATION, PREVIOUS_LOAN
from app.database.crud import save_prediction


def prediction(data, db):
  try:
    if data.Loan_intent not in Loan_intent_freq:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Loan_intent",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(Loan_intent_freq.keys())[:5]
            }
        )

    if data.Home_ownership not in Home_ownership_freq:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid Home_ownership",
                "hint": "Use /options endpoint to see valid values",
                "examples": list(Home_ownership_freq.keys())[:5]
            }
        )


    Loan_intent_val = Loan_intent_freq[data.Loan_intent]
    Home_ownership_val = Home_ownership_freq[data.Home_ownership]

    
    Gender_map = GENDER[data.Gender]
    Education_map = EDUCATION[data.Education]
    Previous_loan_map = PREVIOUS_LOAN[data.Previous_loan_defaults_on_file]

    input_data = pd.DataFrame([{"Age":data.Age,
                                "Gender": Gender_map,
                                "Education": Education_map,
                                "Income": data.Income,
                                "Employment_experience": data.Employment_experience,
                                "Home_ownership": Home_ownership_val,
                                "Loan_amount": data.Loan_amount,
                                "Loan_intent": Loan_intent_val,
                                "Loan_interest_rate": data.Loan_interest_rate,
                                "Loan_percent_income": data.Loan_percent_income,
                                "Credit_history_length": data.Credit_history_length,
                                "Credit_score": data.Credit_score,
                                "Previous_loan_defaults_on_file": Previous_loan_map }])

    input_data = input_data[["Age",
                             "Gender",
                             "Education",
                             "Income",
                             "Employment_experience",
                             "Home_ownership",
                             "Loan_amount",
                             "Loan_intent",
                             "Loan_interest_rate",
                             "Loan_percent_income",
                             "Credit_history_length",
                            "Credit_score",
                            "Previous_loan_defaults_on_file"]]
    scaled_input = scale.transform(input_data)

    prediction = model.predict(scaled_input)[0]

    db_obj = save_prediction(db, data, prediction)

    return {
        "prediction": "Loan_Approved" if prediction == 1 else "Loan_Decline",
        "db_id": db_obj.id
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
