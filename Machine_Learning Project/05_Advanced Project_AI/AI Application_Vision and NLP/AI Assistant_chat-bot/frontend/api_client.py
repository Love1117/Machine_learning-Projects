import requests

FASTAPI_URL = "https://chat-bot-api-ncg1.onrender.com"


def chat_bot(question, image=None, audio=None):

    data = {
        "question": question
    }

    files = {}

    # Image
    if image is not None:
        files["image"] = (
            image.name,
            image.getvalue(),
            image.type
        )

    # Audio
    if audio is not None:
        files["audio"] = (
            "voice.webm",
            audio["bytes"],
            "audio/webm"
        )

    response = requests.post(
        f"{FASTAPI_URL}/chat",
        data=data,
        files=files if files else None
    )

    response.raise_for_status()
    return response.json()
