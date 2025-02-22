from pydantic import BaseModel

class UploadRequest(BaseModel):
    price: int
    image_base64: str