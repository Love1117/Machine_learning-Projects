from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="Mobile Recommendation API",
    version="1.0"
)


@app.get("/")
def home():
    return {"message": "Mobile Recommendation API is running"}
    
app.include_router(router)
