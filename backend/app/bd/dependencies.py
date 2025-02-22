from bd.database import SessionLocal

def get_db():
    """Generador de sesión de base de datos para FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
