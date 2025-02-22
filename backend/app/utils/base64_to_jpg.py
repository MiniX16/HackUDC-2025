import json
import base64
import os

def base64_to_jpg(base64_string, output_path):
    """Convierte una cadena Base64 a una imagen JPG y la guarda en un archivo."""
    try:
        image_data = base64.b64decode(base64_string)
        with open(output_path, "wb") as image_file:
            image_file.write(image_data)
        print(f"Imagen guardada en: {output_path}")
    except Exception as e:
        print(f"Error al convertir la imagen: {e}")

def process_json(input_json, output_folder="images"):
    """Lee un JSON con imágenes en Base64 y las convierte a archivos JPG."""
    # Crear carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)
    
    with open(input_json, "r", encoding="utf-8") as f:
        products = json.load(f)
    
    for product in products:
        image_base64 = product.get("image_base64", "No encontrado")
        if image_base64 != "No encontrado":
            output_path = os.path.join(output_folder, f"{product['id']}.jpg")
            base64_to_jpg(image_base64, output_path)
        else:
            print(f"Imagen no encontrada para {product['name']}")

    print("Proceso completado.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_json(sys.argv[1])
    else:
        print("Uso: python base64_to_jpg.py <archivo_json>")

