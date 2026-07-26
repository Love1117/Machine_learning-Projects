import requests

FASTAPI_URL = "https://text-summarization-api-65g3.onrender.com"

def summarize_text(input_data):
    response = requests.post(
        f"{FASTAPI_URL}/summarize",
        json=input_data
    )
    response.raise_for_status()
    return response.json()
