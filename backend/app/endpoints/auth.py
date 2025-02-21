from fastapi import APIRouter, HTTPException
from services.auth_service import generate_token

router = APIRouter()

@router.get("/get-token/")
async def get_token():
    """Endpoint para obtener el JWT Token de Inditex"""
    try:
        return generate_token()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
