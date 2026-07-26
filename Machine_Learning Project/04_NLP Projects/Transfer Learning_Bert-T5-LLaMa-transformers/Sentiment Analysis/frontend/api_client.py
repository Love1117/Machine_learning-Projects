import requests

FASTAPI_URL = "http://fastapi:8000"

def sentiment(request):
    response = requests.post(
        f"{FASTAPI_URL}/predict-roberta",
        json=request
    )
    response.raise_for_status()
    return response.json()
