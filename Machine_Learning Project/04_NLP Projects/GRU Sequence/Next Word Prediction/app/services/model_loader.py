import joblib
import tensorflow as tf
from tensorflow import keras
import gdown
from app.core.config import MODEL_DIR
import os

BASE_DIR = Path.cwd()
MODEL_DIR = BASE_DIR / "models" / "1st_version"

MODEL_PATH = MODEL_DIR / "GRU_model.keras"
TOKENIZER_PATH = MODEL_DIR / "GRU_tokenizer.pkl"

# 🔹 Google Drive File IDs
MODEL_FILE_ID = "1ZbZ6Hlesmi4MzgmHZIe216-o4LrDMCOi"
TOKENIZER_FILE_ID = "1ZbZ6Hlesmi4MzgmHZIe216-o4LrDMCOi"

def download_from_drive(file_id, output_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, str(output_path), quiet=False)

def ensure_files_exist():
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Download model if not exists
    if not MODEL_PATH.exists():
        print("Downloading model from Google Drive...")
        download_from_drive(MODEL_FILE_ID, MODEL_PATH)

    # Download tokenizer if not exists
    if not TOKENIZER_PATH.exists():
        print("Downloading tokenizer from Google Drive...")
        download_from_drive(TOKENIZER_FILE_ID, TOKENIZER_PATH)

@app.on_event("startup")
def load_resources():
    global model, tokenizer

    ensure_files_exist()

    print("Loading model...")
    model = keras.models.load_model(MODEL_PATH)

    print("Loading tokenizer...")
    tokenizer = joblib.load(TOKENIZER_PATH)

    print("✅ Model and Tokenizer loaded successfully!")
