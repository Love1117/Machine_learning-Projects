import joblib
import tensorflow as tf
from tensorflow import keras
from huggingface_hub import hf_hub_download
import os
from dotenv import load_dotenv


load_dotenv()

HF_GRU_TOKEN = os.getenv("HF_GRU_TOKEN")

REPO_ID = "Love117/lstm-prediction"

MODEL_PATH = hf_hub_download(
    repo_id=REPO_ID,
    filename="my_model_2.keras",
    token=HF_GRU_TOKEN,
)

TOKENIZER_PATH = hf_hub_download(
    repo_id=REPO_ID,
    filename="tokenizer.joblib",
    token=HF_GRU_TOKEN,
)

model = keras.models.load_model(MODEL_PATH)
tokenizer = joblib.load(TOKENIZER_PATH)
