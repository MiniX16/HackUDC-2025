import os
import time
import requests
from config import (
    INDITEX_CLIENT_ID,
    INDITEX_CLIENT_SECRET,
    INDITEX_TOKEN_URL,
    INDITEX_API_URL
)

INDITEX_SEARCH_URL = "https://api.inditex.com/searchpmpa/products"
INDITEX_SEARCH_IMAGE_URL = "https://api.inditex.com/pubvsearch/products"

TOKEN_EXPIRATION_TIME = 3599

def get_api_key():
    """Obtiene la API Key, actualizándola solo si ha caducado."""
    api_key = os.getenv("INDITEX_API_JWT", "").strip()
    expiration = os.getenv("INDITEX_API_EXPIRATION", "0").strip()

    # Verificar si el token aún es válido
    if api_key and time.time() < float(expiration):
        return api_key

    return update_api_key()


def update_api_key():
    """Obtiene un nuevo token de acceso desde la API de Inditex y lo actualiza en el entorno."""
    auth = (INDITEX_CLIENT_ID, INDITEX_CLIENT_SECRET)
    data = {
        "grant_type": "client_credentials",
        "scope": "technology.catalog.read"  # Ajusta los scopes según sea necesario
    }
    headers = {
        "User-Agent": "PostmanRuntime/7.31.1"
    }

    response = requests.post(INDITEX_TOKEN_URL, auth=auth, data=data, headers=headers)

    if response.status_code == 200:
        token_data = response.json()
        id_token = token_data.get("id_token")

        if id_token:
            expiration_time = time.time() + TOKEN_EXPIRATION_TIME  # Forzar expiración a 3599s
            os.environ["INDITEX_API_JWT"] = id_token
            os.environ["INDITEX_API_EXPIRATION"] = str(expiration_time)
            return id_token

    raise Exception(f"Error obteniendo token: {response.status_code} - {response.text}")


def search_products_by_image(image_url):
    """Envía la URL de la imagen a la API de Inditex y devuelve los productos similares."""
    api_key = get_api_key()
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
    api_key = get_api_key()
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    params = {
        "query": query
    }

    response = requests.get(INDITEX_SEARCH_URL, params=params, headers=headers)

    print(response.json())

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en Inditex API: {response.status_code} - {response.text}")

