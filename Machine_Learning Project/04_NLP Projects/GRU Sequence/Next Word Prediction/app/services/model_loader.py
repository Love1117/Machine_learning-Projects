import os
import joblib
from tensorflow import keras
from huggingface_hub import hf_hub_download
from dotenv import load_dotenv

load_dotenv()

HF_GRU_TOKEN = os.getenv("HF_GRU_TOKEN")

if not HF_GRU_TOKEN:
    raise ValueError("HF_GRU_TOKEN not found.")

REPO_ID = "Love117/gru-word-prediction"

model = None
tokenizer = None


def load_resources():
    global model, tokenizer
    print("Step 1")

    model_path = hf_hub_download(
        repo_id=REPO_ID,
        filename="GRU_model.keras",
        token=HF_GRU_TOKEN,
    )
    print("Step 2")

    tokenizer_path = hf_hub_download(
        repo_id=REPO_ID,
        filename="GRU_tokenizer.pkl",
        token=HF_GRU_TOKEN,
    )
    print("Step 3")

    # model = keras.models.load_model(model_path)
    model = None
    
    # tokenizer = joblib.load(tokenizer_path)
    tokenizer = None
    print("Step 4")

    print("✅ GRU model loaded successfully.")
