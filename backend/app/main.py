from fastapi import FastAPI
from endpoints import upload

app = FastAPI()

# Incluir los routers
app.include_router(upload.router, prefix="/api", tags=["upload"])

@app.get("/")
def home():
    return {"message": "API de subida de imágenes con ImgBB"}
