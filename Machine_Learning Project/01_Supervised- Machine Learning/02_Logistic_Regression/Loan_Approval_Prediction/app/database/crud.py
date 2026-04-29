from app.database.models import Prediction
from app.core.constants import GENDER, EDUCATION, PREVIOUS_LOAN


def save_prediction(db, data, prediction):
    db_obj = Prediction(
        Age=data.Age,
        Gender=GENDER[data.Gender],
        Education=EDUCATION[data.Education],
        Income=data.Income,
        Employment_experience=data.Employment_experience,
        Home_ownership=data.Home_ownership,
        Loan_amount=data.Loan_amount,
        Loan_intent=data.Loan_intent,
        Loan_interest_rate=data.Loan_interest_rate,
        Loan_percent_income=data.Loan_percent_income,
        Credit_history_length=data.Credit_history_length,
        Credit_score=data.Credit_score,
        Previous_loan_defaults_on_file=PREVIOUS_LOAN[data.Previous_loan_defaults_on_file]
        Outcome_status=prediction
    )

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
