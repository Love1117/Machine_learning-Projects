import requests

FASTAPI_URL = "http://fastapi:8000"

def predict_salary(data):
    response = requests.post(
        f"{FASTAPI_URL}/predict",
        json=data
    )
    response.raise_for_status()
    return response.json()

def get_options():
    response = requests.get(
        f"{FASTAPI_URL}/options"
    )
    response.raise_for_status()
    return response.json()
    

def get_country():
    response = requests.get(
        f"{FASTAPI_URL}/countries"
    )
    response.raise_for_status()
    return response.json()


def get_race():
    response = requests.get(
        f"{FASTAPI_URL}/racism"
    )
    response.raise_for_status()
    return response.json()

def get_jobs():
    response = requests.get(
        f"{FASTAPI_URL}/job_title"
    )
    response.raise_for_status()
    return response.json()
