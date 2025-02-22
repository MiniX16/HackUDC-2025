import base64
from bs4 import BeautifulSoup
import requests
import re

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
    product_price = "No encontrado"
    if script_tag:
        match = re.search(r'"mainPrice":(\d+\.\d+)', script_tag.text)
        if match:
            product_price = match.group(1)

    # Extraer descripción
    product_description = soup.find("meta", property="og:description")
    product_description = product_description.get("content", "No encontrado") if product_description else "No encontrado"

    # Extraer URL de la imagen principal y convertir a base64
    product_image = soup.find("meta", property="og:image")
    product_image = image_to_base64(product_image["content"]) if product_image else "No encontrado"

    # Extraer URL de la imagen de la prenda y convertir a base64
    image_tag = soup.find("img", class_="media-image__image")
    image_base64 = image_to_base64(image_tag["src"]) if image_tag else "No encontrado"

    # Extraer categoría
    script_category = soup.find("script", text=lambda t: t and "categoryName" in t)
    product_category = "No encontrado"
    if script_category:
        match = re.search(r'"categoryName":"(.*?)"', script_category.text)
        if match:
            product_category = match.group(1)

    # Extraer color
    script_color = soup.find("script", text=lambda t: t and '"color":' in t)
    product_color = "No encontrado"
    if script_color:
        match = re.search(r'"color":"(.*?)"', script_color.text)
        if match:
            product_color = match.group(1)

    # Imprimir resultados
    return {
        "Nombre": product_name,
        "Precio": product_price,
        "Descripción": product_description,
        "Imagen Base64": product_image,
        "Imagen Prenda Base64": image_base64,
        "Categoría": product_category,
        "Color": product_color
    }

# Ejecutar el scraper
result = scrape_zara("pagina_completa.html")
for key, value in result.items():
    print(f"{key}: {value}")

