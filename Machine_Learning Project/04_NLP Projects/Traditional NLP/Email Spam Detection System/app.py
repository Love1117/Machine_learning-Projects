from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import joblib
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"

tfidf_vectorizer = joblib.load(MODEL_DIR / "tfidf_vectorizer.joblib")
model = joblib.load(MODEL_DIR / "Email-spam-detection_V1.0.0.joblib")

class TextInput(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Spam Detection API! Send a POST request to /predict to classify text."}

@app.post("/predict")
async def predict_spam(text_input: TextInput):
    new_vec = tfidf_vectorizer.transform([text_input.text])

    prediction = model.predict(new_vec)

    # Interpret the prediction
    result = "Spam" if prediction[0] == 1 else "Not-Spam"
    
    return {"input_text": text_input.text, "prediction": result}
