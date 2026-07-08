from pathlib import Path
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found. Check your .env file.")
        

SECRET_KEY = os.getenv("MY_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("MY_SECRET_KEY not found. Check your .env file.")


ADMIN_USERNAME = os.getenv("USERNAME")
if not USERNAME:
    raise ValueError("USERNAME not found. Check your .env file.")


ADMIN_PASSWORD = os.getenv("PASSWORD")
if not PASSWORD:
    raise ValueError("PASSWORD not found. Check your .env file.")
