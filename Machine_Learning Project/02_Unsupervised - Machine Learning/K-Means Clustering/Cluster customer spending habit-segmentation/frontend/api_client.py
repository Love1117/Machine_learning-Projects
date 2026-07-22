import requests

FASTAPI_URL = "https://customer-spending-habit-ui.onrender.com"

def predict_spend_habit(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()
