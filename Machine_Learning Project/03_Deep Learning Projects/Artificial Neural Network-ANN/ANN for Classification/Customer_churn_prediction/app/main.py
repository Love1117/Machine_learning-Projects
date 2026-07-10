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
    title="Customer Churn Prediction API",
    description="Production-ready ML API"
)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "FastAPI is running"}

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
class ChurnAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.gender,
        Prediction.SeniorCitizen,
        Prediction.Partner,
        Prediction.Dependents,
        Prediction.tenure,
        Prediction.PhoneService,
        Prediction.MultipleLines,
        Prediction.OnlineSecurity,
        Prediction.OnlineBackup,
        Prediction.DeviceProtection,
        Prediction.TechSupport,
        Prediction.StreamingTV,
        Prediction.StreamingMovies,
        Prediction.PaperlessBilling,
        Prediction.MonthlyCharges,
        Prediction.TotalCharges,
        Prediction.PaymentMethod_status,
        Prediction.Contract_status,
        Prediction.InternetService_status,
        Prediction.prediction,
        Prediction.probability,
    ]

    searchable_columns = [
        Prediction.StreamingTV,
        Prediction.SeniorCitizen,
        Prediction.gender,
        Prediction.PaymentMethod_status,
        Prediction.Contract_status,
        Prediction.InternetService_status,
        Prediction.prediction,
    ]

    page_size = 50

# Add the view to your admin dashboard
admin.add_view(ChurnAdmin)

app.include_router(router)
