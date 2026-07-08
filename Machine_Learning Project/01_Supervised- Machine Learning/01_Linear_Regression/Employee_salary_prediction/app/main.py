from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base
from app.database.session import engine
from app.database.models import Prediction
from sqladmin import Admin, ModelView

app = FastAPI(title="Employee Salary Prediction",
              description="Production Style, ML Project for Employees Salary Prediction",
              version= "v1.0.0")


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
@app.get("/")
def home():
    return{"message": "FastAPI is running successfully"}


admin = Admin(app, engine)

# 4. Tell SQLAdmin how to display your Product table
class EmployeeAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.Age,
        Prediction.Gender,
        Prediction.Education_Level,
        Prediction.Years_of_Experience,
        Prediction.Country,
        Prediction.Race,
        Prediction.Senior,
        Prediction.Job_title,
        Prediction.Employee_Salary,
    ]

    searchable_columns = [
        Prediction.Country,
        Prediction.Job_title,
        Prediction.Gender,
    ]

    page_size = 50

# Add the view to your admin dashboard
admin.add_view(EmployeeAdmin)

app.include_router(router)
