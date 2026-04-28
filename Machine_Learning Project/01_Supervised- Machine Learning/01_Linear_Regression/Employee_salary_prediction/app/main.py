from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine



app = FastAPI(title="Employee Salary Prediction",
              description="Production Style, ML Project for Employees Salary Prediction",
              version= "v1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
app.include_router(router)
