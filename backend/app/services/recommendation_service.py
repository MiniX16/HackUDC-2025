from bd.models import Product
from utils.color_utils import get_matching_colors
from sqlalchemy import func
from sqlalchemy.orm import Session

def get_recommendations_by_id(db: Session, base_product, allowed_categories):
    """Busca productos compatibles y selecciona solo una prenda por categoría desde la BD"""
    base_color = base_product.color.upper()  # Convertimos el color base a mayúsculas
    
    matching_colors = [color.upper() for color in get_matching_colors(base_color)]  # Convertimos todos los colores compatibles a mayúsculas

    print (matching_colors)
    # Obtener productos compatibles desde la BD (misma categoría excluida)
    compatible_products = db.query(Product).filter(
        func.upper(Product.color).in_(matching_colors),  # Comparación en mayúsculas
        Product.category.in_(allowed_categories)
    ).all()

    print (compatible_products)

    # Seleccionar solo una prenda por categoría
    selected_recommendations = {}
    for product in compatible_products:
        category = product.category
        if category not in selected_recommendations:
            selected_recommendations[category] = product

    return list(selected_recommendations.values())  # Devolvemos los productos seleccionados
