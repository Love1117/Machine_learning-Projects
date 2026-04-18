import nest_asyncio
from fastapi import FastAPI
from pydantic import BaseModel
from keras.models import load_model
import joblib
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pathlib import Path
import gdown
import os


nest_asyncio.apply()
app = FastAPI()

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
    model = load_model(MODEL_PATH)

    print("Loading tokenizer...")
    tokenizer = joblib.load(TOKENIZER_PATH)

    print("✅ Model and Tokenizer loaded successfully!")



def predict_next_words(input_word: str, len_of_words: int, tokenizer, model):
  generated_text = input_word

  for _ in range(len_of_words):
    seq = tokenizer.texts_to_sequences([generated_text])[0]

    if len(seq) < 3:
      seq_to_predict = pad_sequences([seq], maxlen=3, padding='pre')[0]
    else:
      seq_to_predict = seq[-3:]

    seq_to_predict = np.array(seq_to_predict)

    if not seq_to_predict.tolist():
        break

    # seq_to_predict is already a 1D numpy array from pad_sequences
    # It needs to be reshaped to (1, 3) for the model input
    if seq_to_predict.shape[0] != 3:
        seq_to_predict = pad_sequences([seq_to_predict], maxlen=3, padding='pre')[0]

    seq_to_predict = seq_to_predict.reshape(1, 3)

    # To Ensure model is loaded
    if model is None:
        return "Error: Model not loaded."

    pred_probs = model.predict(seq_to_predict, verbose=0)
    pred_index = np.argmax(pred_probs, axis=1)[0]

    next_word = ""
    next_word_found = False

    for win, idx in tokenizer.word_index.items():
      if idx == pred_index:
        next_word = win
        next_word_found = True
        break

    if next_word_found:
      generated_text += " " + next_word
    else:
      print(f"Predicted index {pred_index} not found in tokenizer vocabulary. Stopping prediction.")
      break

  return generated_text





class PredictionRequest(BaseModel):
    input_word: str
    len_of_words: int

@app.post("/predict")
async def predict(request: PredictionRequest):
    if model is None or tokenizer is None:
        return {"error": "Model or tokenizer not loaded. Check server logs.", "generated_text": ""}

    try:
        generated_text = predict_next_words(
            input_word=request.input_word,
            len_of_words=request.len_of_words,
            tokenizer=tokenizer,
            model=model
        )
        return {"generated_text": generated_text}
    except Exception as e:
        print(f"Prediction error: {e}")
        import traceback
        traceback_str = traceback.format_exc()
        return {"error": f"An internal error occurred during prediction: {e}", "traceback": traceback_str, "generated_text": ""}
