from bd.models import Product
from utils.color_utils import get_matching_colors
from sqlalchemy import func
from sqlalchemy.orm import Session
import random

def get_recommendations_by_id(db: Session, color, allowed_categories):
    """Busca productos compatibles y selecciona solo una prenda aleatoria por categoría desde la BD"""
    base_color = color.upper()
    matching_colors = [color.upper() for color in get_matching_colors(base_color)]

    compatible_products = db.query(Product).filter(
        func.upper(Product.color).in_(matching_colors),
        Product.category.in_(allowed_categories)
    ).all()

    # Organizar productos por categoría
    category_products = {}
    for product in compatible_products:
        category_products.setdefault(product.category, []).append(product)

    # Seleccionar un producto aleatorio por categoría
    selected_recommendations = [
        random.choice(products) for products in category_products.values()
    ]

    return selected_recommendations
