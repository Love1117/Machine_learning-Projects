from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base, Prediction
from app.database.session import engine
from sqladmin import Admin, ModelView
from app.core.config import SECRET_KEY, ADMIN_USERNAME, ADMIN_PASSWORD
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI(
    title="Heart disease prediction API",
    description="Production-ready ML API"
)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Heart Disease API is running"}


# 2. Create a Secure Admin Login System
class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        # Set your secret admin credentials here.
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            request.session.update({"token": "authenticated_admin_user"})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if token == "authenticated_admin_user":
            return True
        return False

# Initialize the secure authentication backend
authentication_backend = AdminAuth(secret_key=SECRET_KEY)

admin = Admin(app, engine, authentication_backend=authentication_backend)

# 4. Tell SQLAdmin how to display your Product table
class HeartAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.gender,
        Prediction.height,
        Prediction.weight,
        Prediction.systolic_blood_pressure,
        Prediction.diastolic_blood_pressure,
        Prediction.cholesterol,
        Prediction.gluc,
        Prediction.smoke,
        Prediction.alcohol_intake,
        Prediction.Physical_activity,
        Prediction.age,
        Prediction.bmi,
        Prediction.bp_status,
        Prediction.Prediction,
    ]

    searchable_columns = [
        Prediction.alcohol_intake,
        Prediction.smoke,
        Prediction.gender,
        Prediction.bp_status,
    ]

    page_size = 50

# Add the view to your admin dashboard
admin.add_view(HeartAdmin)


app.include_router(router)
