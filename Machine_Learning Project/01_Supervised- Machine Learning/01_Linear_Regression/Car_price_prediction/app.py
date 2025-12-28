from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
  return {"message": "FastAPI API created in Colab"}
