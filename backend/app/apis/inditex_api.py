import os
import requests
from config import (
    INDITEX_CLIENT_ID,
    INDITEX_CLIENT_SECRET,
    INDITEX_TOKEN_URL,
    INDITEX_API_URL
)

INDITEX_SEARCH_URL = "https://api.inditex.com/searchpmpa/products"
INDITEX_SEARCH_IMAGE_URL = "https://api.inditex.com/pubvsearch/products"

def update_api_key():
    """Obtiene un nuevo token de acceso desde la API de Inditex y lo actualiza en el entorno."""
    auth = (INDITEX_CLIENT_ID, INDITEX_CLIENT_SECRET)
    data = {
        "grant_type": "client_credentials",
        "scope": "technology.catalog.read"  # Ajusta los scopes según sea necesario
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.post(INDITEX_TOKEN_URL, auth=auth, data=data, headers=headers)

    if response.status_code == 200:
        token_data = response.json()
        id_token = token_data.get("id_token")
        if id_token:
            os.environ["INDITEX_API_JWT"] = id_token  # Guardar el token en la variable de entorno
            return id_token
    else:
        raise Exception(f"Error obteniendo token: {response.status_code} - {response.text}")


def search_products_by_image(image_url):
    """Envía la URL de la imagen a la API de Inditex y devuelve los productos similares."""
    update_api_key()
    api_key = os.getenv("INDITEX_API_JWT", "").strip()
    print(api_key)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "PostmanRuntime/7.31.1"
    }

    params = {
        "image": image_url 
    }

    response = requests.get(INDITEX_SEARCH_IMAGE_URL, params=params, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")


def search_products_by_text(query):
    """Busca productos en Inditex usando una consulta de texto en lugar de una imagen."""
    api_key = os.getenv("INDITEX_API_JWT", "").strip()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    params = {
        "query": query
    }

    response = requests.get(INDITEX_SEARCH_URL, params=params, headers=headers)

    print(f"Response Status: {response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")

