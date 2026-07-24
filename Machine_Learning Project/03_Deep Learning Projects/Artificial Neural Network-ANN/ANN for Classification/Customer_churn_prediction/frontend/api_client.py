import requests

FASTAPI_URL = "https://customer-chun-prediction-api.onrender.com"

def predict_churn(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()
