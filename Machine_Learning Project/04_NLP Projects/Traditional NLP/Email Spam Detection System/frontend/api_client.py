import requests

FASTAPI_URL = "http://fastapi:8000"

def predict_next_word(text_input):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=text_input
    )
    response.raise_for_status()
    return response.json()
