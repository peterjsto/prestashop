import time
import os
from behave import Given, When, Then
from features.pages.contact import ContactUs
from features.pages.presta_shop import PrestaShopLogin


@Given("El usuario se encuentra en la pagina web")
def el_usuario_se_encuentra_en_la_pagina_web(context):
    context.contact = ContactUs()
    context.contact.abrir_pagina()


@When("Haga clic en Contact Us")
def step_click_contact_us(context):
    context.contact.clic_contacto()  # Uso del contexto para manejar la instancia


@When("Complete el formulario")
def step_fill_form(context):
    context.contact.select_subject("1")  # Selecciona "Customer Service"
    context.contact.ingresar_email("a@mail.com")
    context.contact.ingresar_mensaje("Este es un mensaje de prueba.")


@When('Adjunte un archivo "{archivo}"')
def adjunte_un_archivo(context, archivo):
    file_path = os.path.join(os.getcwd(), archivo)  # Ruta relativa al directorio de pruebas
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo '{file_path}' no existe en la ruta esperada.")
    context.contact.adjuntar_archivo(file_path)


@Then("Podra enviar el formulario")
def step_send_form(context):
    context.contact.enviar_formulario()


@Then("Cerrar el navegador")
def step_close_browser(context):
    context.contact.cerrar()
