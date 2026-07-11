from fastapi import FastAPI
from app.api.routes import router
from app.database.models import Base, Prediction, Prediction2
from app.database.session import engine
from sqladmin import Admin, ModelView
from app.core.config import SECRET_KEY, ADMIN_USERNAME, ADMIN_PASSWORD
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI(
    title="Building Words with Similar meaning API",
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
class SimilarAdmin(ModelView, model=Prediction):
    column_list = [
        Prediction.id,
        Prediction.word,
        Prediction.topn,
        Prediction.similar_words,
    ]

    searchable_columns = [
        Prediction.word
    ]

    page_size = 50

class WordSimilarityAdmin(ModelView, model=Prediction2):
    column_list = [
        Prediction2.id,
        Prediction2.word1,
        Prediction2.word2,
        Prediction2.similarity_score,
    ]

    searchable_columns = [
        Prediction2.word1,
        Prediction2.word2,
    ]

    page_size = 50


# Add the view to your admin dashboard
admin.add_view(SimilarAdmin)
admin.add_view(WordSimilarityAdmin)

app.include_router(router)
