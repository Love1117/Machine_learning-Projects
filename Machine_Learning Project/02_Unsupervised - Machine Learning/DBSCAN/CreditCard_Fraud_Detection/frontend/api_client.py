import requests

FASTAPI_URL = "https://credit-card-fraud-detection-api-hnt3.onrender.com"


def predict_fraud(data):
    try:
        response = requests.post(
            f"{FASTAPI_URL}/predict",
            json=data,
            timeout=60
        )

        # Successful response
        if response.ok:
            return response.json()

        # FastAPI returned an error
        try:
            error_detail = response.json()
        except ValueError:
            error_detail = response.text

        raise Exception(
            f"FastAPI returned HTTP {response.status_code}: {error_detail}"
        )

    except requests.exceptions.Timeout:
        raise Exception(
            "The FastAPI server took too long to respond. "
            "The Render service may be sleeping or unavailable."
        )

    except requests.exceptions.ConnectionError:
        raise Exception(
            "Could not connect to the FastAPI server. "
            "Please check that the Render API is running."
        )

    except requests.exceptions.RequestException as e:
        raise Exception(
            f"Request to FastAPI failed: {str(e)}"
        )
