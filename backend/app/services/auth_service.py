from apis.auth_api import get_auth_token

def generate_token():
    """Llama a la API de autenticación y devuelve el token"""
    return {"access_token": get_auth_token()}
