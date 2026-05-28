from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="Music Recommendation API",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Music Recommendation API is running"}
    
app.include_router(router)