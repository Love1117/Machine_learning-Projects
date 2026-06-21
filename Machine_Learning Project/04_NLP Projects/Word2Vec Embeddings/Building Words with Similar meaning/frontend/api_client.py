import requests

FASTAPI_URL = "http://fastapi:8000"

def similar_word(request):
    response = requests.post(
        f"{FASTAPI_URL}/similar_words",
        json=request
    )
    response.raise_for_status()
    return response.json()


def word_similar(request):
    response = requests.post(
        f"{FASTAPI_URL}/word_similarity",
        json=request
    )
    response.raise_for_status()
    return response.json()
