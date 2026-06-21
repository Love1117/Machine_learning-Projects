from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine



app = FastAPI(
    title="Fraud Detection Prediction API",
    description="Production-ready ML API"
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "FastAPI is running"}
    
app.include_router(router)
