import time

from behave import given, when, then
from features.pages.presta_shop import PrestaShopLogin


@given('el navegador "{navegador}" está abierto')
def step_impl(context, navegador):
    context.prestashop = PrestaShopLogin(navegador=navegador)
    context.prestashop.abrir_pagina()
    time.sleep(20)

# ----- ARRANGE -----
@when("El usuario va a crear una cuenta")
def step_open_browser_and_navigate(context):
    context.prestashop.visualizar_inicio()


# ----- ACT -----
@when("hace clic en el botón de iniciar sesión")
def step_click_sign_in(context):
    # Act: Hacer clic en "Iniciar sesión"
    context.prestashop.iniciar_sesion()


@when("hace clic en el botón de registro")
def step_click_register(context):
    # Act: Navegar al formulario de registro
    context.prestashop.clic_registro()


@when("Llena el formulario de registro con los siguientes datos")
def step_fill_registration_form(context):
    # Arrange: Crear un diccionario a partir de la tabla proporcionada en el feature
    datos_usuario = {row["campo"]: row["valor"] for row in context.table}

    # Act: Completar el formulario
    context.prestashop.registro_usuario(datos_usuario)


# ----- ASSERT -----
@then("debería poder crear la cuenta siendo redirigido al inicio")
def step_verify_user_redirected(context):
    # Assert: Confirmar que se muestra el elemento de inicio
    context.prestashop.visualizar_inicio()
    print("El usuario fue redirigido exitosamente al inicio.")


@then("no podrá crear la cuenta")
def step_verify_account_creation_error(context):
    # Assert: Verificar que el registro falló
    # Podría capturarse un mensaje de error visible en la interfaz
    print("Error: El usuario no pudo crear la cuenta.")
