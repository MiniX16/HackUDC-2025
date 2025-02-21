from fastapi import APIRouter, File, UploadFile, HTTPException
from services.uploadService import process_upload

router = APIRouter()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_url = process_upload(file.file)
        return {"url": image_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
