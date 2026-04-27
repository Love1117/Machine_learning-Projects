from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Car Price Prediction API",
    description="Production-ready ML API"
)

app.include_router(router)
