from apis.uploadApi import upload_to_imgbb

def process_upload(file):
    """Procesa la subida de la imagen y obtiene la URL"""
    return upload_to_imgbb(file)
