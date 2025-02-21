import requests
from config import INDITEX_CLIENT_ID, INDITEX_CLIENT_SECRET, INDITEX_TOKEN_URL

def get_auth_token():
    """Obtiene el JWT Token desde la API de autenticación de Inditex"""
    data = {
        "grant_type": "client_credentials",
        "client_id": INDITEX_CLIENT_ID,
        "client_secret": INDITEX_CLIENT_SECRET
    }

    response = requests.post(INDITEX_TOKEN_URL, data=data)

    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Error obteniendo el token: {response.status_code} - {response.text}")
