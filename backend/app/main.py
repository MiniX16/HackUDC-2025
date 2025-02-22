from fastapi import FastAPI
from endpoints import upload, recommendations
from endpoints.random_products import router as random_products_router  # Importa solo el router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite peticiones desde este origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)


# Incluir los routers correctamente
app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(recommendations.router, prefix="/api", tags=["recommendations"])
app.include_router(random_products_router, prefix="/api", tags=["random-products"])  # Ahora sí importa el router correctamente

@app.get("/")
def home():
    return {"message": "API de recomendaciones de moda"}
