from fastapi import APIRouter, HTTPException, Query
from services.randomProducts_service import get_random_products

router = APIRouter()

@router.get("/random-products/")
async def get_random_products_list(n: int = Query(..., gt=0)):  # Nuevo nombre de función
    """Endpoint que devuelve n productos aleatorios del dataset"""
    try:
        products = get_random_products(n)
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
