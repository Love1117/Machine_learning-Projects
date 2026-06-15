import requests

FASTAPI_URL = "http://fastapi:8000"

def predict_car(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )

    return response.json()


def get_car_models():
    response = requests.get(
        f"{FASTAPI_URL}/car_models"
    )
    return response.json()


def get_car_names():
    response = requests.get(
        f"{FASTAPI_URL}/car_names"
    )
    return response.json()
