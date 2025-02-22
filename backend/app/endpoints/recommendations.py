from fastapi import APIRouter, HTTPException, Query
from services.randomProducts_service import get_random_products

router = APIRouter()  # Asegúrate de definir el router aquí

@router.get("/random-products/")
async def get_random_products_endpoint(n: int = Query(..., gt=0)):
    """Endpoint que devuelve n productos aleatorios del dataset"""
    try:
        products = get_random_products(n)
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
