import requests

FASTAPI_URL = "http://fastapi:8000"

def hand_digit(file):
    response = requests.post(
        f"{FASTAPI_URL}/predict_image",
        json=file
    )
    response.raise_for_status()
    return response.json()
