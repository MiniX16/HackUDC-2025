from fastapi import FastAPI
from endpoints import upload, recommendations
from endpoints.random_products import router as random_products_router  # Importa solo el router
from fastapi.middleware.cors import CORSMiddleware
from bd.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Incluir los routers correctamente
app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(recommendations.router, prefix="/api", tags=["recommendations"])
app.include_router(random_products_router, prefix="/api", tags=["random-products"])

@app.get("/")
def home():
    return {"message": "API de recomendaciones de moda"}
