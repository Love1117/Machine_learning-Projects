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
    title="Fraud Detection Prediction API",
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
class FraudAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.click_duration,
        Prediction.scroll_depth,
        Prediction.mouse_movement,
        Prediction.keystrokes_detected,
        Prediction.click_frequency,
        Prediction.time_since_last_click,
        Prediction.VPN_usage,
        Prediction.proxy_usage,
        Prediction.bot_likelihood_score,
        Prediction.year,
        Prediction.month,
        Prediction.day,
        Prediction.days_of_the_week,
        Prediction.hour,
        Prediction.weekend,
        Prediction.device_type_status,
        Prediction.device_ip_reputation_status,
        Prediction.browser_status,
        Prediction.operating_system_status,
        Prediction.ad_position_status,
        Prediction.prediction,
        Prediction.probability,
    ]

    searchable_columns = [
        Prediction.VPN_usage,
        Prediction.year,
        Prediction.days_of_the_week,
        Prediction.weekend,
        Prediction.device_type_status,
        Prediction.device_ip_reputation_status,
        Prediction.browser_status,
        Prediction.operating_system_status,
        Prediction.ad_position_status,
        Prediction.prediction,
    ]

    page_size = 50

# Add the view to your admin dashboard
admin.add_view(FraudAdmin)


app.include_router(router)
