from apis.uploadApi import upload_to_imgbb
from apis.inditex_api import search_products_by_image
from bd.crud import get_product_by_id
from bd.database import SessionLocal
from utils.get_html import get_html
from utils.img_scrapper import scrape_zara

def process_upload(image_base64, price):
    """Sube la imagen a ImgBB, obtiene su URL y busca productos en Inditex."""
    image_url = upload_to_imgbb(image_base64)
    products = search_products_by_image(image_url)

    # Filtrar productos por precio
    filtered_products = [
        product for product in products if product["price"]["value"]["current"] <= price or price == 0
    ]

    scrapped_prod = []
    for prod in filtered_products:
        html = get_html(prod["link"])
        sc_product = scrape_zara(html)
        if sc_product["Imagen Prenda Base64"] != "No encontrado":
            scrapped_prod.append(sc_product)
        if len(scrapped_prod) >= 1:
            break

    return [{
        "id": prod["id"],
        "name": sc_prod["Nombre"],
        "currency": prod["price"]["currency"],
        "description": sc_prod["Descripción"],
        "link": prod["link"],
        "brand": prod["brand"],
        "image_base64": sc_prod["Imagen Prenda Base64"],
        "category": sc_prod["Categoría"],
        "color": sc_prod["Color"]
        }
    for prod, sc_prod in zip(filtered_products[:1], scrapped_prod[:1])]
