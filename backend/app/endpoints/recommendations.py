from fastapi import APIRouter, HTTPException
from services.recommendation_service import get_recommendations_by_id
from bd.crud import get_product_by_id
from bd.database import SessionLocal

router = APIRouter()

# Categorías principales para completar un outfit
MAIN_CATEGORIES = ["t-shirt", "jacket", "pants", "shoes", "coat"]

@router.get("/recommendations/")
async def get_recommendations_endpoint(id: int):
    """Endpoint que obtiene recomendaciones basadas en un producto en la BD"""
    with SessionLocal() as db:
        base_product = get_product_by_id(db, id)  # Buscar en la BD por ID

        if not base_product:
            raise HTTPException(status_code=404, detail="No se encontró el producto en la BD")

        base_category = base_product.category

        # Determinar qué categorías incluir en la recomendación
        if base_category in MAIN_CATEGORIES:
            # Si el producto pertenece a una categoría clave, excluimos esa y tomamos las demás
            categories_to_include = [cat for cat in MAIN_CATEGORIES if cat != base_category]
        else:
            # Si el producto no pertenece a ninguna categoría clave, usamos todas
            categories_to_include = MAIN_CATEGORIES

        recommendations = get_recommendations_by_id(db, base_product, categories_to_include)

    return recommendations
