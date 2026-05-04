import pandas as pd
from fastapi import HTTPException

from app.services.model_loader import model
from app.core.constants import Classes
from app.database.crud import save_prediction
