const { Builder } = require('selenium-webdriver');
const firefox = require('selenium-webdriver/firefox');

const options = new firefox.Options();

// Cambia la ruta a la de tu geckodriver si es necesario
const driver = new Builder()
    .forBrowser('firefox')
    .setFirefoxOptions(options)
    .setFirefoxService(new firefox.ServiceBuilder(new firefox.ServiceBuilder('C:\\Users\\User\\Downloads\\geckodriver-v0.35.0-win64\\geckodriver.exe'))) // Cambia esta ruta en Windows a 'C:\\Program Files\\geckodriver.exe'
    .build();

(async function test() {
    try {
        await driver.get('https://www.google.com'); // Abre Google
        console.log('Página abierta correctamente');
    } catch (error) {
        console.error('Error:', error);
    } finally {
        await driver.quit();
    }
})();
