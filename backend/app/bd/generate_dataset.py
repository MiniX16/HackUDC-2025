from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from get_html import get_html
from img_scrapper import scrape_zara

# Configurar la base de datos
DATABASE_URL = "sqlite:///products.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definir la tabla de productos
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=True)
    currency = Column(String, nullable=True)
    description = Column(String, nullable=True)
    image_base64 = Column(String, nullable=True)
    color = Column(String, nullable=True)
    category = Column(String, nullable=True)
    link = Column(String, nullable=False, unique=True)
    brand = Column(String)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

def process_products(json_file, max_retries=3):
    """Lee un JSON con productos, obtiene el HTML y extrae los datos para almacenarlos en la BD."""
    with open(json_file, "r", encoding="utf-8") as f:
        products = json.load(f)
    
    for product in products:
        url = product["link"]
        print(f"Procesando: {url}")
        
        retries = 0
        while retries < max_retries:
            get_html(url)  # Obtener el HTML de la página
            product_info = scrape_zara("pagina_completa.html")  # Extraer la información
            print(product_info)
            
            if product_info.get("Imagen Base64", "No encontrado") != "No encontrado":
                new_product = Product(
                    id=product["id"],
                    name=product["name"],
                    price=product["price"]["value"]["current"],
                    currency=product["price"]["currency"],
                    description=product_info.get("Descripción", ""),
                    image_base64=product_info.get("Imagen Base64", ""),
                    color=product_info.get("Color", "Desconocido"),
                    category=product_info.get("Categoría", "Desconocida"),
                    link=url,
                    brand=product["brand"]
                )
                session.add(new_product)
                session.commit()
                break  # Salir del bucle si se obtiene la información correcta
            
            print(f"Reintentando {retries + 1}/{max_retries} para {url}")
            retries += 1
        
        if retries == max_retries:
            print(f"No se pudo obtener información para {url}, omitiendo...")
    
    print("Proceso completado. Todos los productos válidos han sido almacenados en la BD.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        process_products(sys.argv[1])
    else:
        print("Uso: python store_products_sqlalchemy.py <archivo_json>")

