import requests

FASTAPI_URL = "https://credit-card-fraud-detection-api-hnt3.onrender.com"

def predict_fraud(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()
    
