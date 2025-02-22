import requests
from config import IMGBB_API_KEY

IMGBB_UPLOAD_URL = "https://api.imgbb.com/1/upload"

def upload_to_imgbb(image_base64):
    """Sube una imagen en Base64 a ImgBB y devuelve la URL de la imagen."""
    data = {
        "key": IMGBB_API_KEY,
        "image": image_base64
    }

    response = requests.post(IMGBB_UPLOAD_URL, data=data)
    data = response.json()

    if response.status_code == 200:
        return data["data"]["url"]
    else:
        raise Exception(f"Error subiendo a ImgBB: {data['error']['message']}")
