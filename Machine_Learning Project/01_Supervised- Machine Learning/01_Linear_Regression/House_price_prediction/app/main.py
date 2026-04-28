from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine



app = FastAPI(title="House Price Prediction API",
              description="Production Style, Machine learning for house price prediction",
              version="version1.0.0.0")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
app.include_router(router)
