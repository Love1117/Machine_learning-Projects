import os
import joblib
from tensorflow import keras
from huggingface_hub import hf_hub_download
from dotenv import load_dotenv

load_dotenv()

HF_GRU_TOKEN = os.getenv("HF_GRU_TOKEN")

if not HF_GRU_TOKEN:
    raise ValueError("HF_GRU_TOKEN not found.")

REPO_ID = "Love117/lstm-prediction"

model = None
tokenizer = None


def load_resources():
    global model, tokenizer

    model_path = hf_hub_download(
        repo_id=REPO_ID,
        filename="my_model_2.keras",
        token=HF_GRU_TOKEN,
    )

    tokenizer_path = hf_hub_download(
        repo_id=REPO_ID,
        filename="tokenizer.joblib",
        token=HF_GRU_TOKEN,
    )

    model = keras.models.load_model(model_path)
    tokenizer = joblib.load(tokenizer_path)

    print("✅ GRU model loaded successfully.")
