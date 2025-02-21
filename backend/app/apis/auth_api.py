import requests
from requests.auth import HTTPBasicAuth
from config import INDITEX_CLIENT_ID, INDITEX_CLIENT_SECRET, INDITEX_TOKEN_URL

def get_auth_token():
    response = requests.post(
        INDITEX_TOKEN_URL,
        auth=HTTPBasicAuth(INDITEX_CLIENT_ID, INDITEX_CLIENT_SECRET),  
        data={"grant_type": "client_credentials", "scope": "technology.stock.read"}
    )

    if response.status_code == 200:
        return response.json()
    
    raise Exception(f"Error {response.status_code}: {response.text}")
