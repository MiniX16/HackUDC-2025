import json
from utils.color_utils import get_matching_colors

# Cargar dataset
with open("data/output.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

# Categorías obligatorias en la recomendación
REQUIRED_CATEGORIES = ["pants", "shoes", "accessory"]

def find_product_by_url(url):
    """Busca una prenda en el dataset usando la URL"""
    for product in dataset:
        if product["link"] == url:
            return product
    return None

def get_recommendations_by_url(product_url):
    """Busca productos compatibles y selecciona solo una prenda por categoría"""
    base_product = find_product_by_url(product_url)
    
    if not base_product:
        return {"error": "Producto no encontrado en el dataset"}
    
    base_color = base_product["color"]
    base_category = base_product["category"]
    
    matching_colors = get_matching_colors(base_color)

    # Filtrar productos compatibles por color
    compatible_products = [
        product for product in dataset
        if product["color"] in matching_colors and product["category"] != base_category
    ]

    # Seleccionar solo una prenda por categoría diferente
    selected_recommendations = {}
    for product in compatible_products:
        category = product["category"]
        if category not in selected_recommendations:
            selected_recommendations[category] = product  # Guardamos solo el primer producto de cada categoría

    # Rellenar las categorías faltantes con opciones neutras del dataset
    for required_category in REQUIRED_CATEGORIES:
        if required_category not in selected_recommendations:
            for product in dataset:
                if product["category"] == required_category:
                    selected_recommendations[required_category] = product
                    break  # Solo necesitamos un producto por categoría

    return list(selected_recommendations.values())  # Devolvemos los productos seleccionados
