import requests
from config import IMGBB_API_KEY

IMGBB_UPLOAD_URL = "https://api.imgbb.com/1/upload"

def upload_to_imgbb(image_file):
    """Sube una imagen a ImgBB y devuelve la URL"""
    files = {"image": image_file}
    params = {"key": IMGBB_API_KEY}

    response = requests.post(IMGBB_UPLOAD_URL, params=params, files=files)
    data = response.json()

    if response.status_code == 200:
        return data["data"]["url"]
    else:
        raise Exception(data["error"]["message"])
