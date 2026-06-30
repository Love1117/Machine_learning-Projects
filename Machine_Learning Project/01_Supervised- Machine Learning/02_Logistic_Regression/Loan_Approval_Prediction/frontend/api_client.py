import requests

FASTAPI_URL = "https://loan-prediction-api-eu4s.onrender.com"

def loan_approval(data):
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
