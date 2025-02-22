import requests
from config import INDITEX_API_JWT

INDITEX_SEARCH_URL = "https://api.inditex.com/searchpmpa/products"
INDITEX_SEARCH_IMAGE_URL = "https://api.inditex.com/pubvsearch/products"

def search_products_by_image(image_url):
    """Envía la URL de la imagen a la API de Inditex y devuelve los productos similares."""
    headers = {
        "Authorization": f"Bearer {INDITEX_API_JWT.strip()}",
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.31.1"
    }

    params = {
        "image": image_url 
    }

    response = requests.get(INDITEX_SEARCH_IMAGE_URL, params=params, headers=headers)

    print(f"Response Status: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")

def search_products_by_text(query):
    """Busca productos en Inditex usando una consulta de texto en lugar de una imagen."""
    headers = {
        "Authorization": f"Bearer {INDITEX_API_JWT.strip()}",
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.31.1"
    }

    params = {
        "query": query
    }

    response = requests.get(INDITEX_SEARCH_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")
