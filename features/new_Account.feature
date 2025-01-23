
Feature: Usuario se crea una cuenta correctamente
    Scenario: Usuario se registra con datos válidos
        Given el navegador "firefox" está abierto
        When El usuario va a crear una cuenta
        And hace clic en el botón de iniciar sesión
        And hace clic en el botón de registro
        And Llena el formulario de registro con los siguientes datos:
          | campo         | valor          |
          | first_name    | Fede           |
          | last_name     | López          |
          | email         | fede@email.com |
          | password      | Feder@a.-q123. |
          | birth_date    | 01/01/1990     |
        Then debería poder crear la cuenta siendo redirigido al inicio

    Scenario Outline: Usuario se registra con datos diferentes
        Given el navegador "chrome" está abierto
        When El usuario va a crear una cuenta
        When hace clic en el botón de iniciar sesión
        And hace clic en el botón de registro
        And Llena el formulario de registro con los siguientes datos:
            | campo         | valor       |
            | first_name    | <nombre>   |
            | last_name     | <apellido> |
            | email         | <email>    |
            | password      | <password> |
            | birth_date    | <fecha>    |
        Then debería poder crear la cuenta siendo redirigido al inicio

        Examples:
            | nombre        | apellido    | email                   | password           | fecha      |
            | Fede          | López       | fede@email.com          | Feder@a.-q123.     | 01/01/1990 |
            | Ana           | Fernández   | ana_fernandez@email.com | AnaFern4ndez123.   | 10/10/1985 |