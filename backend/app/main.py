from fastapi import FastAPI
from endpoints import upload, auth

app = FastAPI()

# Incluir los routers
app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])

@app.get("/")
def home():
    return {"message": "API de subida de imágenes con búsqueda en Inditex"}
