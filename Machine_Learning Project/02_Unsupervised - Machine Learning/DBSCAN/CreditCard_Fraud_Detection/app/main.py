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
    title="CreditCard Fraud Detection API",
    description="Production-ready ML API"
)

app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
@app.get("/")
def home():
    return {"message":"FastAPI is running successfully"}


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
class CredictCardAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.step,
        Prediction.amount,
        Prediction.oldbalanceOrg,
        Prediction.newbalanceOrig,
        Prediction.oldbalanceDest,
        Prediction.newbalanceDest,
        Prediction.status_type,
        Prediction.Is_fraud,
    ]

    searchable_columns = [
        Prediction.status_type,
        Prediction.Is_fraud,
    ]

    page_size = 50

# Add the view to your admin dashboard
admin.add_view(CredictCardAdmin)


app.include_router(router)
