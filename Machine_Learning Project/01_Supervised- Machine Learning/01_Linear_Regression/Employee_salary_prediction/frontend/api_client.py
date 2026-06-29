import requests

FASTAPI_URL = "https://employee-salary-prediction-1mmm.onrender.com"

def predict_salary(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()

def get_options():
    response = requests.get(
        f"{FASTAPI_URL}/options"
    )
    response.raise_for_status()
    return response.json()
