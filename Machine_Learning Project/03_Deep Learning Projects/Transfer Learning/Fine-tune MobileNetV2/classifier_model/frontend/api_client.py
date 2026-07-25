import requests

FASTAPI_URL = "https://image-classifier-api-5d5f.onrender.com"

def image_animal(file):

    files = {
        "file": (file.name,
                 file.getvalue(),
                 file.type)
    }

    response = requests.post(
        f"{FASTAPI_URL}/predict",
        files=files
    )

    response.raise_for_status()
    return response.json()
