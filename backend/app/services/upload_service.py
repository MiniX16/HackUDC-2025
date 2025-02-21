from apis.uploadApi import upload_to_imgbb
from apis.inditex_api import search_products_by_image

def process_upload(file, access_token):
    """Sube la imagen a ImgBB y luego la usa para buscar productos en Inditex"""
    image_url = upload_to_imgbb(file)
    products = search_products_by_image(image_url, access_token)
    
    return {
        "image_url": image_url,
        "products": products
    }
