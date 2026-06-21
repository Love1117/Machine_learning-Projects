import requests

FASTAPI_URL = "http://fastapi:8000"

def predict_next_word(request):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=request
    )
    response.raise_for_status()
    return response.json()
