import joblib
import tensorflow as tf
from tensorflow import keras
from huggingface_hub import hf_hub_download
import os

HF_GRU_TOKEN = os.getenv("HF_GRU_TOKEN")

REPO_ID = "Love117/gru-word-prediction"

MODEL_PATH = hf_hub_download(
    repo_id=REPO_ID,
    filename="GRU_model.keras",
    token=HF_GRU_TOKEN,
)

TOKENIZER_PATH = hf_hub_download(
    repo_id=REPO_ID,
    filename="GRU_tokenizer.pkl",
    token=HF_GRU_TOKEN,
)

model = keras.models.load_model(MODEL_PATH)
tokenizer = joblib.load(TOKENIZER_PATH)
