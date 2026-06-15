import requests

FASTAPI_URL = "http://fastapi:8000"

def predict_car(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )

    return response.json()
