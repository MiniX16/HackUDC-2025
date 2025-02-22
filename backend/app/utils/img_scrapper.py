import base64
from bs4 import BeautifulSoup
import requests

def image_to_base64(image_url):
    """Descarga una imagen desde una URL y la convierte a Base64."""
    response = requests.get(image_url)
    if response.status_code == 200:
        encoded_string = base64.b64encode(response.content).decode("utf-8")
        return encoded_string
    return "No encontrado"

def scrape_zara(html_file):
    with open(html_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extraer nombre del producto
    product_name = soup.find("meta", property="og:title")
    product_name = product_name["content"] if product_name else "No encontrado"

    # Extraer precio
    script_tag = soup.find("script", string=lambda t: t and "mainPrice" in t)
    if script_tag:
        import re
        match = re.search(r'"mainPrice":(\d+\.\d+)', script_tag.text)
        product_price = match.group(1) if match else "No encontrado"
    else:
        product_price = "No encontrado"

    # Extraer descripción
    product_description = soup.find("meta", property="og:description")
    product_description = product_description.get("content", "No encontrado") if product_description else "No encontrado"

    # Extraer URL de la imagen principal y convertir a base64
    product_image = soup.find("meta", property="og:image")
    product_image = image_to_base64(product_image["content"]) if product_image else "No encontrado"

    # Extraer URL de la imagen de la prenda y convertir a base64
    image_tag = soup.find("img", class_="media-image__image")

    print(image_tag)
    image_base64 = image_to_base64(image_tag["src"]) if image_tag else "No encontrado"

    # Extraer categoría
    product_category = soup.find("script", text=lambda t: t and "categoryName" in t)
    if product_category:
        match = re.search(r'"categoryName":"(.*?)"', product_category.text)
        product_category = match.group(1) if match else "No encontrado"
    else:
        product_category = "No encontrado"

    # Imprimir resultados
    return {
        "Nombre": product_name,
        "Precio": product_price,
        "Descripción": product_description,
        "Imagen Base64": product_image,
        "Imagen Prenda Base64": image_base64,
        "Categoría": product_category
    }

# Ejecutar el scraper
result = scrape_zara("pagina_completa.html")
for key, value in result.items():
    print(f"{key}: {value}")

