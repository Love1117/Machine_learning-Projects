import requests

FASTAPI_URL = "http://fastapi:8000"

def chat_bot(request):
    response = requests.post(
        f"{FASTAPI_URL}/chat",
        json=request
    )
    response.raise_for_status()
    return response.json()
