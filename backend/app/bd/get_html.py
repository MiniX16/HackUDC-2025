from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

def get_html(url, output_file="pagina_completa.html"):
    """Obtiene el HTML de una URL y lo guarda en un archivo."""
    
    # Configurar opciones de Firefox
    options = Options()
    options.headless = True  # Ejecutar en segundo plano
    options.add_argument("--headless")
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/120.0")  # Evitar detección de bot
    
    # Ruta de geckodriver (ajústala si es necesario)
    #service = Service("C:/Users/User/Downloads/geckodriver-v0.35.0-win64/geckodriver.exe")# Cambia esto si es diferente en tu sistema
    service = Service(GeckoDriverManager().install())



    # Iniciar el navegador
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)
    
    # Esperar a que la página cargue completamente
    time.sleep(5)
    
    # Obtener el HTML completo
    html = driver.page_source
    
    # Guardar el HTML en un archivo
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    driver.quit()
    print(f"Página guardada con éxito en {output_file}")
    return html

# Ejemplo de uso
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
        get_html(url)
    else:
        print("Uso: python get_html.py <URL>")

