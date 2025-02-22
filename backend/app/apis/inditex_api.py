import requests
from config import INDITEX_API_JWT

INDITEX_SEARCH_URL = "https://api.inditex.com/searchpmpa/products?query=shirt"

def search_products_by_image(image_url):
    """Envía la URL de la imagen a la API de Inditex y devuelve los productos similares."""
    headers = {
        "Authorization": f"Bearer {INDITEX_API_JWT}",
        "Content-Type": "application/json"
    }

    params = {
        "image": image_url
    }

    response = requests.get(INDITEX_SEARCH_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")
