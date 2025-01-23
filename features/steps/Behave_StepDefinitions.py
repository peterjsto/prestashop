from behave import Given, When, Then
from selenium import webdriver


@Given('el navegador "{browser}" está abierto')
def step_impl(context, browser):
    if browser.lower() == "chrome":
        context.driver = webdriver.Chrome()
    elif browser.lower() == "firefox":
        context.driver = webdriver.Firefox()
    else:
        raise ValueError(f"Navegador '{browser}' no es soportado")
    context.driver.maximize_window()


@When('el usuario navega a "{url}"')
def step_impl(context, url):
    context.driver.get(url)


@Then('el título de la página debe ser "{title}"')
def step_impl(context, title):
    assert context.driver.title == title, f"El título esperado era '{title}', pero era '{context.driver.title}'"
    context.driver.quit()
