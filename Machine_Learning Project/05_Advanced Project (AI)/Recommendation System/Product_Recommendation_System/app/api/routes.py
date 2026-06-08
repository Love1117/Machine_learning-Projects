from fastapi import APIRouter
from app.schemas.product_schema import ProductRequest
from app.services.product_service import recommend_products
from app.services.model_loader import products 



router = APIRouter()



@router.get("/model_check")
def model_check():
    return {"status": "ok"}


@router.get("/mobile")
def get_products():
    product_category = products["category"].tolist()
    return {
        "category": product_category
    }

@router.post("/recommend")
def get_product_recommendations(request: ProductRequest):
    return recommend_products(request.category)
