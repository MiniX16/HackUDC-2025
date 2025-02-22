import base64
from bs4 import BeautifulSoup
import requests
import re
from collections import Counter


CATEGORIES = [
    "t-shirt", "tee", "shirt", "blouse", "sweater", "pullover", "jumper", "jacket", 
    "coat", "hoodie", "tank top", "camisole", "cardigan", "vest", "anorak", "parka", 
    "windbreaker", "blazer", "poncho", "polo", "crop top", "sleeveless top",
    "pants", "trousers", "jeans", "denim", "shorts", "bermuda", "culottes", "leggings", 
    "joggers", "sweatpants", "capris", "cargo pants", "chinos", "track pants",
    "dress", "gown", "jumpsuit", "romper", "overalls", "dungarees", "playsuit",
    "bra", "bralette", "panties", "knickers", "thong", "boxers", "briefs", "boxer briefs", 
    "slip", "underwear", "corset", "bustier", "long johns", "pajamas", "nightgown", 
    "nightdress", "robe", "kimono", "negligee", "sleepwear",
    "shoes", "sneakers", "trainers", "boots", "sandals", "flip-flops", "loafers", 
    "moccasins", "heels", "stilettos", "pumps", "oxfords", "derbies", "espadrilles", 
    "clogs", "slippers", "wedges",
    "hat", "cap", "beanie", "beret", "fedora", "visor", "sunhat", "scarf", "gloves", 
    "mittens", "belt", "tie", "bowtie", "necktie", "bandana", "shawl", "wrap", "headband", 
    "earmuffs", "suspenders", "stockings", "tights", "leggings", "socks"
]

def find_most_common_category(html_text):
    """Encuentra la palabra de la lista de categorías que aparece más veces en el HTML."""
    text = html_text.lower()
    counts = Counter(word for word in CATEGORIES if word in text)
    return counts.most_common(1)[0][0] if counts else "No encontrado"


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
    product_category = find_most_common_category(soup.text)

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

