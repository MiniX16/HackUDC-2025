from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.upload_service import process_upload
from models.UploadRequest import UploadRequest
router = APIRouter()


@router.post("/upload-image/")
async def upload_image(request: UploadRequest):
    """Endpoint para subir imagen en Base64 y buscar productos en Inditex"""
    try:
        products = process_upload(request.image_base64, request.price)
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
