import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

class ShoppingCart:

    #XPATHS

    PRODUCT_HUMMINGBIRD_XPATH = "//article[@data-id-product='2'][1]"
    ADD_TO_CART_BUTTON_XPATH = "//button[@data-button-action='add-to-cart']"
    PROCEED_TO_CHECKOUT_XPATH = "//a[text()='Proceed to checkout']"
    CONTINUE_SHOPPING_XPATH = "//button[@class='btn btn-secondary']"
    PRODUCT_HUMMINGBIRD2_XPATH = "//img[@alt='Hummingbird printed t-shirt']"
    INCREASE_QUANTITY_BUTTON_XPATH = "//button[@class='btn btn-touchspin js-touchspin js-increase-product-quantity bootstrap-touchspin-up']"
    COMPANY_FIELD_XPATH = "//input[@id='field-company']"
    VAT_NUMBER_FIELD_XPATH = "//input[@id='field-vat_number']"
    ADDRESS_FIELD_XPATH = "//input[@id='field-address1']"
    ADDRESS_COMPLEMENT_FIELD_XPATH = "//input[@id='field-address2']"
    POSTCODE_FIELD_XPATH = "//input[@id='field-postcode']"
    CITY_FIELD_XPATH = "//input[@id='field-city']"
    PHONE_FIELD_XPATH = "//input[@id='field-phone']"
    BUTTON_CONTINUE_XPATH = "//button[@class='continue btn btn-primary float-xs-right']"
    DELIVERY_CHECKBOX_XPATH = "//input[@id='delivery_option_2']"
    BANK_WIRE_PAYMENT_XPATH = "//input[@data-module-name='ps_wirepayment']"
    AGREE_CHECKBOX_XPATH = "//label[@class='js-terms']"
    PLACE_ORDER_BUTTON_XPATH = "//button[@class='btn btn-primary center-block']"
    ORDER_CONFIRMED_XPATH = "//i[@class='material-icons rtl-no-flip done']"
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

    def esperar_elemento(self, xpath, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        except Exception as e:
                print(f"Error al esperar el elemento con XPath {xpath}: {e}")
                raise

        # Métodos para acciones específicas
    def add_product(self):
            self.driver.refresh()
            iframe = WebDriverWait(self.driver, 10).until(
                 EC.presence_of_element_located((By.XPATH, self.IFRAME_XPATH))
             )
            self.driver.switch_to.frame(iframe)
            time.sleep(4)
            """Añade un producto al carrito."""
            product = self.esperar_elemento(self.PRODUCT_HUMMINGBIRD_XPATH)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
            time.sleep(2)
            product.click()
            time.sleep(7)
            add_to_cart_button = self.esperar_elemento(self.ADD_TO_CART_BUTTON_XPATH)
            add_to_cart_button.click()
            time.sleep(5)

    def proceed_to_checkout(self):
            """Procede al checkout desde el carrito."""
            proceed_to_checkout = self.esperar_elemento(self.PROCEED_TO_CHECKOUT_XPATH)
            proceed_to_checkout.click()
            time.sleep(2)

    def button_continue(self):
            """boton para continuar"""
            continue_button = self.esperar_elemento(self.BUTTON_CONTINUE_XPATH)
            continue_button.click()
            time.sleep(2)

    def fill_address(self, company, address, postcode, city, phone):
            """Llena los campos requeridos para la dirección de envío."""
            self.esperar_elemento(self.COMPANY_FIELD_XPATH).send_keys(company)
            self.esperar_elemento(self.ADDRESS_FIELD_XPATH).send_keys(address)
            self.esperar_elemento(self.POSTCODE_FIELD_XPATH).send_keys(postcode)
            self.esperar_elemento(self.CITY_FIELD_XPATH).send_keys(city)
            self.esperar_elemento(self.PHONE_FIELD_XPATH).send_keys(phone)

    def continue_shopping(self):
            """Hace clic en el botón 'Continuar'."""
            button_continue_shopping = self.esperar_elemento(self.CONTINUE_SHOPPING_XPATH)
            button_continue_shopping.click()
            time.sleep(2)

    def add_another_product(self):
            """Añade un producto al carrito."""
            product2 = self.esperar_elemento(self.PRODUCT_HUMMINGBIRD2_XPATH)
            product2.click()
            time.sleep(3)
            add_to_cart_button = self.esperar_elemento(self.ADD_TO_CART_BUTTON_XPATH)
            add_to_cart_button.click()
            time.sleep(2)

    def select_shipping_method(self):
            """Selecciona el método de envío."""
            delivery_checkbox = self.esperar_elemento(self.DELIVERY_CHECKBOX_XPATH)
            delivery_checkbox.click()

    def select_payment_method(self):
            """Selecciona el método de pago."""
            bank_wire_payment = self.esperar_elemento(self.BANK_WIRE_PAYMENT_XPATH)
            bank_wire_payment.click()

    def agree_to_terms(self):
            """Acepta los términos y condiciones."""
            agree_checkbox = self.esperar_elemento(self.AGREE_CHECKBOX_XPATH)
            agree_checkbox.click()

    def place_order(self):
            """Confirma el pedido."""
            place_order_button = self.esperar_elemento(self.PLACE_ORDER_BUTTON_XPATH)
            place_order_button.click()
            time.sleep(2)

    def verify_order_confirmation(self):
            """Verifica que el pedido haya sido confirmado."""
            order_confirmed = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.ORDER_CONFIRMED_XPATH))
            )
            return order_confirmed.is_displayed()

