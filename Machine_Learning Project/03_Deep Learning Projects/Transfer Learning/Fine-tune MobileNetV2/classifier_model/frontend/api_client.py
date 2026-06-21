import requests

FASTAPI_URL = "http://fastapi:8000"

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
