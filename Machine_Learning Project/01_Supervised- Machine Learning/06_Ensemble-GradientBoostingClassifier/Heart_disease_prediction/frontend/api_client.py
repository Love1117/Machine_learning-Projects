import requests

FASTAPI_URL = "https://heart-disease-prediction-api-bbdf.onrender.com"

def predict_disease(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()
