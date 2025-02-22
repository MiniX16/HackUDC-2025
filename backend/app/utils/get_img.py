import sys
import asyncio
from playwright.async_api import async_playwright

async def get_product_image(url):
    """Extrae la imagen principal de un producto en la web de Zara usando Playwright."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Cambia a True para ejecución en segundo plano
        page = await browser.new_page()
        await page.goto(url, wait_until="load")  # Espera a que la página se cargue completamente

        # Esperar a que la imagen del producto esté visible en la página
        await page.wait_for_selector('img')

        # Buscar la imagen principal
        image_element = await page.query_selector('img')
        image_url = await image_element.get_attribute('src') if image_element else None

        await browser.close()
        return image_url

async def main():
    if len(sys.argv) < 2:
        print("Uso: python get_img.py <URL_DEL_PRODUCTO>")
        sys.exit(1)

    url = sys.argv[1]
    image_url = await get_product_image(url)

    if image_url:
        print("URL de la imagen del producto:", image_url)
    else:
        print("No se pudo encontrar la imagen.")

if __name__ == "__main__":
    asyncio.run(main())

