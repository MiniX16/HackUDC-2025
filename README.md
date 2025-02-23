# HackUDC-2025
---

# **Indeeptex - Búsqueda Inteligente de Moda** 👕🔍  

### Encuentra prendas similares a partir de una imagen y recibe recomendaciones personalizadas.  

---

## **📌 Descripción**  
**Indeeptex** es una plataforma que permite a los usuarios encontrar prendas similares a partir de una imagen, utilizando la **API de InditexTech** para buscar productos dentro del catálogo de Inditex. Además, ofrece recomendaciones personalizadas basadas en **armonía de colores, categorías y precios**, ayudando a los usuarios a crear outfits completos.  

Este proyecto combina un **backend en FastAPI** con un **frontend en React**, junto con web scraping y bases de datos para mejorar la precisión de las recomendaciones.  

---

## **🚀 Funcionalidades**  

✅ **Búsqueda de prendas por imagen** 📸  
✅ **Recomendaciones basadas en armonía de colores y categorías** 🎨  
✅ **Filtrado por precio** 💰  
✅ **Almacenamiento de productos en base de datos para optimizar consultas** 🗄️  
✅ **Web scraping para mejorar la información de los productos** 🌐  

---

## **🛠️ Tecnologías Utilizadas**  

### **Backend**  
- **FastAPI** – Para la API y gestión de solicitudes.  
- **SQLite** – Para almacenamiento de productos y optimización de recomendaciones.  
- **OAuth2** – Para la autenticación con la API de InditexTech.  
- **Selenium** – Para el web scraping de información adicional.  

### **Frontend**  
- **React** – Para la interfaz de usuario.  
- **React Query** – Para la gestión eficiente de datos y caché.  

### **Otras Herramientas**  
- **Uvicorn** – Servidor ASGI para correr FastAPI.  
- **ImgBB API** – Para almacenar temporalmente imágenes subidas por el usuario.  
- **GitHub Actions** – Para integración y despliegue continuo.  
- **Docker** – Para contenedorización del entorno.  

---

## **📌 Instalación y Configuración**  

### **1️⃣ Clonar el repositorio**  
```bash
git clone https://github.com/tu-usuario/indeeptex.git
cd indeeptex
```

### **2️⃣ Configurar el entorno**  

#### **Backend**  
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
Crear un archivo `.env` en `backend/app/config.py` con las siguientes variables:  
```ini
IMGBB_API_KEY=27cb3e6e85cb8e60e3430ee3e69a10fb

# Credenciales de Inditex OAuth2
INDITEX_API_JWT="tu_token_aquí"
INDITEX_CLIENT_ID="tu_client_id"
INDITEX_CLIENT_SECRET="tu_client_secret"
IMGBB_API_KEY="tu_api_key_imgbb"
```

#### **Frontend**  
```bash
cd frontend
npm install
```

---

## **🖥️ Ejecución del Proyecto**  

### **1️⃣ Iniciar el Backend**  
```bash
cd backend/app
uvicorn app.main:app --reload
```
Acceder a la documentación interactiva de la API en:  
📌 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

### **2️⃣ Iniciar el Frontend**  
```bash
cd frontend
npm run dev
```
Abrir en el navegador:  
📌 [http://localhost:5173](http://localhost:5173)  

---

## **📌 Desafíos enfrentados**  
🔐 **Autenticación con OAuth2** – Gestionar la autenticación con la API de InditexTech y la actualización automática del token JWT.  

🌐 **Web Scraping en Inditex** – Superamos las restricciones de la web utilizando Selenium para extraer datos adicionales.  

📱 **Optimización del frontend** – Diseñamos una interfaz en React que permite navegación fluida y respuestas rápidas.  

📝 **Arquitectura escalable** – Diseñamos un sistema modular con almacenamiento en SQLite para optimizar la búsqueda y recomendaciones.  

---

## **🤝 Contribuciones**  
Si quieres contribuir, ¡eres bienvenido! Puedes enviar un **pull request** o abrir un **issue** en GitHub.  
