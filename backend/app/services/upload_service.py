from apis.uploadApi import upload_to_imgbb
from apis.inditex_api import search_products_by_image

def process_upload(image_base64, price):
    """Sube la imagen a ImgBB, obtiene su URL y busca productos en Inditex."""
    image_url = upload_to_imgbb(image_base64)  # Subir imagen a ImgBB y obtener la URL
    products = search_products_by_image(image_url)  # Buscar productos en Inditex con la URL

    # Filtrar productos por precio
    filtered_products = [product for product in products if product["price"]["value"]["current"] <= price or price == 0]

    return filtered_products  # Devolver solo productos con precio menor o igual al límite
