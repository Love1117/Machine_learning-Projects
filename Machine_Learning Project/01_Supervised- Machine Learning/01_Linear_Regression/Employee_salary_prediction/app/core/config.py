from pathlib import Path
import os
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_DIR = BASE_DIR / "models" / "1st_version"
DATABASE_URL = "sqlite:///./employee_salary_prediction.db"



load_dotenv()

SECRET_KEY = os.getenv("MY_SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("MY_SECRET_KEY not found. Check your .env file.")
  
