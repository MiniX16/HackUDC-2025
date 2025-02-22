from fastapi import APIRouter, HTTPException
from services.upload_service import process_upload

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(price: int, image_base64: str):
    """Endpoint para subir imagen en Base64 y buscar productos en Inditex"""
    try:
        products = process_upload(image_base64, price)
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
