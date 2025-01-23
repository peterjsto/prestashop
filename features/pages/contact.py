import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class ContactUs:
    # XPATHS como atributos de clase
    CONTACTUS_TEXT_XPATH = "//a[text()='Contact us']"
    SUBJECT_SELECT_XPATH = "//select[@name='id_contact']"
    EMAIL_INPUT_XPATH = "//input[@id='email']"
    MESSAGE_TEXTAREA_XPATH = "//textarea[@id='contactform-message']"
    ATTACHMENT_TEXT_XPATH = "//input[@id='file-upload']"
    SEND_BUTTON_XPATH = "//input[@value='Send']"
    MESSAGE_SENT_XPATH = "//li[text()='Your message has been successfully sent to our team.']"
    ERROR_MESSAGE_XPATH = "//div[@class='alert alert-danger']"
    IFRAME_XPATH = "//iframe[@id='framelive']"

    def __init__(self, navegador='chrome'):
        if navegador.lower() == 'chrome':
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
        elif navegador.lower() == 'firefox':
            from webdriver_manager.firefox import GeckoDriverManager
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Navegador no soportado: {navegador}")

    def abrir_pagina(self):
            self.driver.get("https://demo.prestashop.com/#/en/front")
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.IFRAME_XPATH))
            )
            self.driver.switch_to.frame(iframe)



    def esperar_elemento(self, xpath, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
            print(f"Error al esperar el elemento con XPath {xpath}: {e}")
            raise

    def clic_contacto(self):
            contact_us_button = self.esperar_elemento(self.CONTACTUS_TEXT_XPATH)
            contact_us_button.click()


    def select_subject(self, value="1"):
        try:
            subject_dropdown = self.esperar_elemento(self.SUBJECT_SELECT_XPATH)
            select = Select(subject_dropdown)
            select.select_by_value(value)
        except Exception as e:
            print(f"Error al seleccionar el asunto: {e}")
            raise

    def ingresar_email(self, email):
        try:
            email_input = self.esperar_elemento(self.EMAIL_INPUT_XPATH)
            email_input.clear()
            email_input.send_keys(email)
        except Exception as e:
            print(f"Error al ingresar el email: {e}")
            raise

    def ingresar_mensaje(self, mensaje):
        try:
            message_box = self.esperar_elemento(self.MESSAGE_TEXTAREA_XPATH)
            message_box.clear()
            message_box.send_keys(mensaje)
        except Exception as e:
            print(f"Error al ingresar el mensaje: {e}")
            raise

    def adjuntar_archivo(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo '{file_path}' no existe.")
        try:
            file_upload = self.esperar_elemento(self.ATTACHMENT_TEXT_XPATH)
            file_upload.send_keys(file_path)
        except Exception as e:
            print(f"Error al adjuntar el archivo: {e}")
            raise

    def enviar_formulario(self):
        try:
            send_button = self.esperar_elemento(self.SEND_BUTTON_XPATH)
            send_button.click()
        except Exception as e:
            print(f"Error al enviar el formulario: {e}")
            raise

    def validar_envio_exitoso(self):
        try:
            mensaje_exitoso = self.esperar_elemento(self.MESSAGE_SENT_XPATH, timeout=10)
            return mensaje_exitoso.is_displayed()
        except Exception:
            return False

    def obtener_mensaje_error(self):
        try:
            error = self.esperar_elemento(self.ERROR_MESSAGE_XPATH, timeout=5)
            return error.text
        except Exception:
            return None

    def cerrar(self):
        self.driver.quit()
