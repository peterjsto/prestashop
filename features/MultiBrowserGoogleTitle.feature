#Feature: Prueba multiplataforma de navegadores
  #Scenario Outline: Verificar el título de Google en diferentes navegadores
   # Given el navegador "<browser>" está abierto
    #When el usuario navega a "https://www.google.com"
    #Then el título de la página debe ser "Google"

  # Examples:
    #| browser  |
    #| chrome   |
    #| firefox  |