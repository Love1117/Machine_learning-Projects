import requests

FASTAPI_URL = "https://house-price-prediction-api-i7r2.onrender.com"

def predict_house_price(data):
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
