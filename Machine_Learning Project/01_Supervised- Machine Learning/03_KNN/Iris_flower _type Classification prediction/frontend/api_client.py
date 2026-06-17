import requests

FASTAPI_URL = "http://fastapi:8000"

def iris_flower(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()
