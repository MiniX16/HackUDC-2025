from fastapi import APIRouter, File, UploadFile, HTTPException
import requests
import os

router = APIRouter()

IMGBB_API_KEY = "27cb3e6e85cb8e60e3430ee3e69a10fb"
IMGBB_UPLOAD_URL = "https://api.imgbb.com/1/upload"

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        files = {"image": file.file}
        params = {"key": IMGBB_API_KEY}

        response = requests.post(IMGBB_UPLOAD_URL, params=params, files=files)
        data = response.json()

        if response.status_code == 200:
            return {"url": data["data"]["url"]}
        else:
            raise HTTPException(status_code=400, detail=data["error"]["message"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
