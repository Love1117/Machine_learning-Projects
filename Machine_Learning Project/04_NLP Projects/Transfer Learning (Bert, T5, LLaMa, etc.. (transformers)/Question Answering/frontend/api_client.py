import requests

FASTAPI_URL = "http://fastapi:8000"

def question(question_data):
    response = requests.post(
        f"{FASTAPI_URL}/predict_answer",
        json=question_data
    )
    response.raise_for_status()
    return response.json()


def get_main_questions():
    response = requests.get(
        f"{FASTAPI_URL}/questions"
    )
    response.raise_for_status()
    return response.json()
