import requests

FASTAPI_URL = "https://credit-card-fraud-detection-api-hnt3.onrender.com"


def predict_fraud(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data,
        timeout=60
    )

if response.status_code != 200:
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    raise Exception(
        f"FastAPI Error {response.status_code}: {response.text}")
