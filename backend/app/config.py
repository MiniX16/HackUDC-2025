import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Configuración de ImgBB
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

# Configuración de Inditex OAuth2
INDITEX_CLIENT_ID = os.getenv("INDITEX_CLIENT_ID")
INDITEX_CLIENT_SECRET = os.getenv("INDITEX_CLIENT_SECRET")
INDITEX_TOKEN_URL = os.getenv("INDITEX_TOKEN_URL")
INDITEX_API_URL = os.getenv("INDITEX_API_URL")
