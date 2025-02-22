import json
from get_html import get_html
from img_scrapper import scrape_zara

def process_products(json_file, output_json="output.json", max_retries=3):
    """Lee un JSON con productos, obtiene el HTML y extrae las imágenes en base64, reintentando si no se encuentran. 
       Si tras todos los intentos no se consigue la imagen, elimina el producto del resultado."""
    with open(json_file, "r", encoding="utf-8") as f:
        products = json.load(f)
    
    filtered_products = []  # Lista para almacenar solo los productos con imagen válida
    
    for product in products:
        url = product["link"]
        print(f"Procesando: {url}")
        
        retries = 0
        while retries < max_retries:
            get_html(url)
            product_info = scrape_zara("pagina_completa.html")
            image_base64 = product_info.get("Imagen Base64", "No encontrado")
            
            if image_base64 != "No encontrado":
                product["image_base64"] = image_base64
                filtered_products.append(product)  # Agregar producto solo si tiene imagen válida
                break  # Salir del bucle si se encuentra la imagen
            
            print(f"Reintentando {retries + 1}/{max_retries} para {url}")
            retries += 1
        
        if retries == max_retries:
            print(f"Eliminando producto {product['name']} por no encontrar imagen")
    
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(filtered_products, f, indent=4, ensure_ascii=False)
    
    print(f"Archivo guardado en {output_json} con {len(filtered_products)} productos válidos")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_products(sys.argv[1])
    else:
        print("Uso: python generate_dataset.py <archivo_json>")

