from apis.auth_api import get_auth_token

def generate_token():
    """Llama a la API de autenticación y devuelve el token con su metadata"""
    return get_auth_token()
