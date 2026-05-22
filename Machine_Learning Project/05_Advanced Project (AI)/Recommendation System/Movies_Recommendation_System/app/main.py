from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Production-ready ML API"
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movie Recommendation API!"}
    
app.include_router(router)
