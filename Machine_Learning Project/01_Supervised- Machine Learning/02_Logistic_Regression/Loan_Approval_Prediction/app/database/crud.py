from app.database.models import Prediction

def save_prediction(db, data, prediction):

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
        car_price=prediction
    )

        Age = data.Age,
        Gender = 1 if data.Gender == "Male" else 0,,
        Education = Education_map,
        Income = data.Income,
        Employment_experience = data.Employment_experience,
        Home_ownership = data.Home_ownership,
        Loan_amount = data.Loan_amount,
        Loan_intent = data.Loan_intent,
        Loan_interest_rate = data.Loan_interest_rate,
        Loan_percent_income = data.Loan_percent_income,
        Credit_history_length = data.Credit_history_length,
        Credit_score = data.Credit_score,
        Previous_loan_defaults_on_file = Previous_loan_map



  
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)

    return db_obj
