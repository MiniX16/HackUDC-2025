import json
import random
from bd.crud import get_random_products_from_db
from bd.database import SessionLocal

def get_random_products(n: int):
    """Devuelve n productos aleatorios de la base de datos."""
    with SessionLocal() as db:
        random_products = get_random_products_from_db(db, n)

        return [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "currency": product.currency,
                "description":product.description,
                "link": product.link,
                "brand": product.brand,
                "image_base64": product.image_base64,
                "category": product.category,
                "color": product.color
            }
            for product in random_products
        ]