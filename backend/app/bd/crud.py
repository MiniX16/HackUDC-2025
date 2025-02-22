from sqlalchemy.orm import Session
from bd.models import Product

def create_product(db: Session, product_data: dict):
    """Guarda un producto en la base de datos."""
    db_product = Product(
        id=product_data["id"],
        name=product_data["name"],
        price=product_data["price"]["value"]["current"],
        currency=product_data["price"]["currency"],
        link=product_data["link"],
        brand=product_data["brand"],
        image_base64=product_data["image_base64"],
        category=product_data["category"],
        color=product_data["color"]
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products_by_price(db: Session, max_price: float):
    """Obtiene productos con precio menor o igual al especificado."""
    return db.query(Product).filter(Product.price <= max_price).all()

def get_products_by_category(db: Session, category: str):
    """Obtiene productos de una categoría específica."""
    return db.query(Product).filter(Product.category == category).all()

def get_product_by_id(db: Session, product_id: str):
    """Obtiene un producto por su ID."""
    return db.query(Product).filter(Product.id == product_id).first()
