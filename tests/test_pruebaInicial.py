import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

"""
ESTO ES UN EJEMPLO DE
LA ANATOMIA DE UN CASO DE PRUEBA
CON PYTEST Y SELENIUM. 

NO ES UN CASO REAL Y NO SE DEBE 
DE EJECUTAR CON PYTEST
"""

# Inicializar instancia de Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Fixture para inicializar y finalizar el navegador
@pytest.fixture
def browser():
  # Setup: codigo para iniciar el navegador utilizando webdriver manager
  driver = webdriver.Chrome(ChromeDriverManager().install())
  yield driver
  # Teardown: Cerrar el navegador despues de la prueba

# Marker personalizado para pruebas E2E
"""
Los markers sirven para agrupar los casos de prueba, en caso de que tengamos muchos casos que probar, podremos agruparlos y ejecutar solamente los markers que queramos.
"""
#@pytest.mark.e2e
def test_home_page_title(browser):
  # Navegar a la pagina de inicio
  browser.get("https://www.ejemploloco.com")

  # Realizar la prueba (assertion)
  assert "Bienvenido a Ejemplo Loco" in browser.title

  # Interaccion con elementos web (ejemplo, hacer clic en un boton)
  login_button = browser.find_element_by_id("login")
  login_button.click()

  # Verificar que la pagina de login se haya cargado
  assert "Iniciar sesion" in browser.page_source