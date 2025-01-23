import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

XPATHS = {
    "iframe": "//iframe[@id='framelive']",
    "products": "//section[@class='featured-products clearfix']//h2[@class='h2 products-section-title text-uppercase']",
    "sign_in": "//span[text()='Sign in']",
    "register": "//a[@data-link-action='display-register-form']",
    "first_name": "//input[@id='field-firstname']",
    "last_name": "//input[@id='field-lastname']",
    "email": "//input[@id='field-email']",
    "password": "//input[@id='field-password']",
    "birth_date": "//input[@id='field-birthday']",
    "checkboxes": [
        "//input[@name='optin']",
        "//input[@name='psgdpr']",
        "//input[@name='newsletter']",
        "//input[@name='customer_privacy']",
    ],
    "save_button": "//button[@type='submit']",
}


class PrestaShopLogin:
    def __init__(self, navegador='chrome'):
        if navegador.lower() == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        elif navegador.lower() == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Navegador no soportado: {navegador}")

    # ----- ARRANGE -----
    def abrir_pagina(self):
        try:
            self.driver.get("https://demo.prestashop.com/#/en/front")
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["iframe"]))
            )
            self.driver.switch_to.frame(iframe)
            print("Página cargada correctamente.")
        except WebDriverException as e:
            print(f"Error al cargar la página: {e}")
            self.cerrar_sesion()
            exit()

    def esperar_elemento(self, xpath, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            print(f"Error esperando elemento ({xpath}): {e}")
            self.cerrar_sesion()
            exit()

    # ----- ACT -----
    def iniciar_sesion(self):
        self.esperar_elemento(XPATHS["sign_in"]).click()
        time.sleep(2)

    def clic_registro(self):
        self.esperar_elemento(XPATHS["register"]).click()

    def registro_usuario(self, datos_usuario):
        try:
            mapeo_campos = {
                "first_name": XPATHS["first_name"],
                "last_name": XPATHS["last_name"],
                "email": XPATHS["email"],
                "password": XPATHS["password"],
                "birth_date": XPATHS["birth_date"],
            }
            # Completar campos de texto
            for campo, valor in datos_usuario.items():
                self._ingresar_texto(mapeo_campos[campo], valor)

            # Manejar checkboxes
            for checkbox in XPATHS["checkboxes"]:
                self.esperar_elemento(checkbox).click()

            # Clic en el botón "guardar"
            self.esperar_elemento(XPATHS["save_button"]).click()
        except Exception as e:
            print(f"Error durante el registro: {e}")
            self.cerrar_sesion()
            exit()

    def _ingresar_texto(self, xpath, texto):
        campo = self.esperar_elemento(xpath)
        campo.clear()
        campo.send_keys(texto)

    # ----- ASSERT -----
    def visualizar_inicio(self):
        assert self.esperar_elemento(XPATHS["products"]) is not None, \
            "Página de inicio no está visibl."

    def cerrar_sesion(self):
        self.driver.quit()
