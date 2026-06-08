from fastapi import APIRouter
from app.schemas.mobile_schema import MobileRequest
from app.services.mobile_service import recommend_phones
from app.services.model_loader import phone_data



router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.get("/mobile")
def get_mobiles():
    brands = phone_data["brand"].tolist()
    return {
        "brands": brands
    }

@router.post("/recommend")
def get_mobile_recommendations(request: MobileRequest):
    return recommend_phones(request.brand)
