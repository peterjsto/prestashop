Feature: Usar el formulario de contacto
  Scenario: El usuario completa y envía el formulario correctamente
    Given El usuario se encuentra en la pagina web
    When Haga clic en Contact Us
    And Complete el formulario
    And Adjunte un archivo "cuenta.txt"
    Then Podra enviar el formulario