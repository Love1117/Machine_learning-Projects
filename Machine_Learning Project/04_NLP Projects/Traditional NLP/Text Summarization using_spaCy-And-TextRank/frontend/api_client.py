import requests

FASTAPI_URL = "http://fastapi:8000"

def summarize_text(input_data):
    response = requests.post(
        f"{FASTAPI_URL}/summarize",
        json=input_data
    )
    response.raise_for_status()
    return response.json()
