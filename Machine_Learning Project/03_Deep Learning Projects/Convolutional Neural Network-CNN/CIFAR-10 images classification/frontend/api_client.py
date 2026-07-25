import requests

FASTAPI_URL = "https://cifar10-image-api.onrender.com"

def image_class(file):

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
