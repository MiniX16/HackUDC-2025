from sqlalchemy import Column, String, Float
from bd.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float, index=True)
    currency = Column(String)
    description = Column(String, nullable = True)
    link = Column(String, unique=True)
    brand = Column(String)
    image_base64 = Column(String)
    category = Column(String, index=True)
    color = Column(String, index=True)
