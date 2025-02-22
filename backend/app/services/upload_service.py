from apis.uploadApi import upload_to_imgbb
from apis.inditex_api import search_products_by_image
from utils.image_utils import image_url_to_base64

def process_upload(image_base64, price):
    """Sube la imagen en Base64 a ImgBB y usa su URL para buscar productos en Inditex."""
    image_url = upload_to_imgbb(image_base64)
    products = search_products_by_image(image_url)  # Buscar productos en Inditex

    filtered_products = []

    for product in products:
        if product["price"]["value"]["current"] <= price:  # Filtrar por precio
            product["image_base64"] = image_url_to_base64(product["link"])
            filtered_products.append(product)

    return filtered_products  # Devuelve solo los productos filtrados
