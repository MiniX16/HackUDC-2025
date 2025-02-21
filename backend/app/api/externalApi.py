import httpx

BASE_URL = "https://api.ejemplo.com"

async def get_data(endpoint: str, params: dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

async def post_data(endpoint: str, payload: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/{endpoint}", json=payload)
        response.raise_for_status()
        return response.json()
