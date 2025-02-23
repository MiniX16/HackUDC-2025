from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.recommendation_service import get_recommendations_by_id
from bd.dependencies import get_db

router = APIRouter()

MAIN_CATEGORIES = ["t-shirt", "jacket", "pants", "shoes", "hoodie"]

@router.get("/recommendations/")
async def get_recommendations_endpoint(color: str, category: str, db: Session = Depends(get_db)):
    """Endpoint que obtiene recomendaciones basadas en un producto en la BD"""

    # Determinar qué categorías incluir en la recomendación
    if category in MAIN_CATEGORIES:
        categories_to_include = [cat for cat in MAIN_CATEGORIES if cat != category]
    else:
        categories_to_include = MAIN_CATEGORIES

    recommendations = get_recommendations_by_id(db, color, categories_to_include)
    return recommendations
