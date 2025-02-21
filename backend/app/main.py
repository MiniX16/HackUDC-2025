from fastapi import FastAPI
from routers import upload

app = FastAPI()

# Incluir el router
app.include_router(upload.router, prefix="/api", tags=["upload"])

@app.get("/")
def home():
    return {"message": "API de subida de imágenes con ImgBB"}
