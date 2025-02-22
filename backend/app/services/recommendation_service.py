from bd.models import Product
from utils.color_utils import get_matching_colors

def get_recommendations_by_id(db, base_product, allowed_categories):
    """Busca productos compatibles y selecciona solo una prenda por categoría desde la BD"""
    base_color = base_product.color
    
    matching_colors = get_matching_colors(base_color)

    # Obtener productos compatibles desde la BD (misma categoría excluida)
    compatible_products = db.query(Product).filter(
        Product.color.in_(matching_colors),
        Product.category.in_(allowed_categories)
    ).all()

    # Seleccionar solo una prenda por categoría
    selected_recommendations = {}
    for product in compatible_products:
        category = product.category
        if category not in selected_recommendations:
            selected_recommendations[category] = product

    return list(selected_recommendations.values())  # Devolvemos los productos seleccionados
