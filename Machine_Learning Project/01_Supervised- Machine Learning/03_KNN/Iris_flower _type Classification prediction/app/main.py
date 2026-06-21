from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine



app = FastAPI(title= "FastAPI for iris Flower type prediction",
              version="v1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Iris flower type is running"}
    
app.include_router(router)
