import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_scenario(context, scenario):
    # Configuración básica, elige el navegador basado en el contexto del escenario
    browser_name = scenario.name.split(' ')[-1].lower()  # Obtén el nombre del navegador del outline
    if browser_name == "chrome":
        chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")  # Opcional: iniciar maximizado
        context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        time.sleep(1)

    elif browser_name == "firefox":
        firefox_service = FirefoxService(executable_path=GeckoDriverManager().install())
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--start-maximized")  # Opcional: iniciar maximizado
        context.driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
        time.sleep(1)

    else:
        raise Exception(f"¡El navegador '{browser_name}' no está soportado!")


def after_scenario(context, scenario):
    # Cierra el navegador después del escenario
    if context.driver:
        context.driver.quit()