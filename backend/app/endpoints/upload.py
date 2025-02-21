from fastapi import APIRouter, File, UploadFile, HTTPException
from services.upload_service import process_upload

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        result = process_upload(file.file)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
from fastapi import APIRouter, File, UploadFile, HTTPException, Query
from services.upload_service import process_upload

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(
    file: UploadFile = File(...),
    access_token: str = Query(...)
):
    """Endpoint para subir imagen y buscar productos en Inditex (requiere JWT Token)"""
    try:
        result = process_upload(file.file, access_token)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
