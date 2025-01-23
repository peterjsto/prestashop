from behave import when, then
from features.pages.shopping_cart import ShoppingCart


# Paso 1: Añado el producto al carrito
@when('Añado el producto al carrito')
def step_add_product_to_cart(context):
    # Lógica para añadir el producto al carrito
    context.shopping_cart = ShoppingCart()
    context.shopping_cart.add_product()

@when('Añado otro producto al carrito')
def step_add_another_product_to_cart(context):
    # Lógica para añadir el producto al carrito
    context.shopping_cart.add_another_product()


# Paso 2: Procedo al checkout
@when('Procedo al checkout')
def step_proceed_to_checkout(context):
    # Lógica para proceder al proceso de checkout
    context.shopping_cart.proceed_to_checkout()

@when('Le doy clic a continuar comprando')
def step_continue_shopping(context):
    # Lógica para proceder al proceso de checkout
    context.shopping_cart.continue_shopping()


# Paso 3: Lleno la dirección de envío
@when('Lleno la direccion de envio con:')
def step_fill_shipping_address(context):
    # Recolecta los datos de la tabla gherkin
    for row in context.table:
        context.shopping_cart.fill_address(
            company=row['company'],
            address=row['address'],
            postcode=row['postcode'],
            city=row['city'],
            phone=row['phone']
        )


# Paso 4: Elijo el método de envío
@when('Elijo el metodo de envio')
def step_choose_shipping_method(context):
    # Lógica para seleccionar el método de envío
    context.shopping_cart.select_shipping_method()
    context.shopping_cart.button_continue()


# Paso 5: Elijo el método de pago
@when('Elijo el metodo de pago')
def step_choose_payment_method(context):
    # Lógica para elegir el método de pago
    context.shopping_cart.select_payment_method()
    context.shopping_cart.agree_to_terms()
    context.shopping_cart.button_continue()


# Paso 6: Podré realizar la compra
@then('Podre realizar la compra')
def step_complete_purchase(context):
    # Lógica para confirmar que la compra fue realizada exitosamente
    assert context.shopping_cart.complete_purchase() == True


