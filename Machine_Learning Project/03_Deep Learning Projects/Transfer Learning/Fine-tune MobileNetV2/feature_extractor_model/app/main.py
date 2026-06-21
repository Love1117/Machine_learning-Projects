from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine



app = FastAPI(
        title="Flower Photo classification API",
        version="1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "Flower Photo FastAPI is Running!"}


app.include_router(router)
