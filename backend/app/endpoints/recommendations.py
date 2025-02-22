from fastapi import APIRouter, HTTPException, Query
from services.recommendation_service import get_recommendations_by_url
from apis.inditex_api import search_products_by_image

router = APIRouter()

@router.get("/recommendations/")
async def get_recommendations_endpoint(image_url: str = Query(...)):
    """Endpoint que obtiene recomendaciones basadas en una imagen"""
    try:
        # Obtener información del producto desde Inditex API
        base_product = search_products_by_image(image_url)

        if not base_product:
            raise HTTPException(status_code=404, detail="No se encontró el producto")

        recommendations = get_recommendations_by_url(base_product)

        return recommendations
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
