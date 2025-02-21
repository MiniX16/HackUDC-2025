import requests
from config import INDITEX_API_URL

def search_products_by_image(image_url: str, access_token: str):
    """Envía la URL de la imagen a la API de Inditex con el JWT Token recibido por parámetro"""
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    params = {"image": image_url}

    response = requests.get(INDITEX_API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error en la API de Inditex: {response.status_code} - {response.text}")
