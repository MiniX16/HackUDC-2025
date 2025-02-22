from apis.uploadApi import upload_to_imgbb
from apis.inditex_api import search_products_by_image
from bd.crud import get_product_by_id
from bd.database import SessionLocal

def process_upload(image_base64, price):
    """Sube la imagen a ImgBB, obtiene su URL y busca productos en Inditex."""
    image_url = upload_to_imgbb(image_base64)
    products = search_products_by_image(image_url)

    # Filtrar productos por precio
    filtered_products = [
        product for product in products if product["price"]["value"]["current"] <= price or price == 0
    ]

    # Manejo eficiente de la base de datos con `with SessionLocal()`
    with SessionLocal() as db:
        return [
            {
                "id": db_product.id,
                "name": db_product.name,
                "price": db_product.price,
                "currency": db_product.currency,
                "description":db_product.description,
                "link": db_product.link,
                "brand": db_product.brand,
                "image_base64": db_product.image_base64,
                "category": db_product.category,
                "color": db_product.color
            } if (db_product := get_product_by_id(db, product["id"])) else product
            for product in filtered_products
        ]
