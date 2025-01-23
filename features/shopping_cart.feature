Feature: Usuario realiza el flujo de compra
  Scenario: Usuario realiza una orden por 1 producto
    Given el navegador "firefox" está abierto
        When El usuario va a crear una cuenta
        And hace clic en el botón de iniciar sesión
        And hace clic en el botón de registro
        And Llena el formulario de registro con los siguientes datos:
          | campo         | valor          |
          | first_name    | carrito          |
          | last_name     | López          |
          | email         | fed@email.com |
          | password      | Feder@a.-q123. |
          | birth_date    | 01/01/1990     |
        And Añado el producto al carrito
        And Procedo al checkout
        And Lleno la direccion de envio con:
          | company       | address         | postcode | city           | phone       |
          | Mi Empresa S.A.| Calle Falsa 123| 12345    | Ciudad Ejemplo | +34123456789|
        And Elijo el metodo de envio
        And Elijo el metodo de pago
        Then Podre realizar la compra

  Scenario: Usuario realiza una orden por varios productos
    Given el navegador "chrome" está abierto
        When El usuario va a crear una cuenta
        And hace clic en el botón de iniciar sesión
        And hace clic en el botón de registro
        And Llena el formulario de registro con los siguientes datos:
          | campo         | valor          |
          | first_name    | Fede           |
          | last_name     | López          |
          | email         | julio@mail.com |
          | password      | Feder@a.-q123. |
          | birth_date    | 01/01/1990     |
        And Añado el producto al carrito
        And Le doy clic a continuar comprando
        And Añado otro producto al carrito
        And Procedo al checkout
        And Lleno la direccion de envio con:
          | company       | address         | postcode | city           | phone       |
          | Mi Empresa S.A.| Calle Falsa 123| 12345    | Ciudad Ejemplo | +34123456789|
        And Elijo el metodo de envio
        And Elijo el metodo de pago
        Then Podre realizar la compra