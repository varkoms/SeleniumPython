import pytest
import allure

@pytest.mark.sandbox
def test_click_en_enviar(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.click_enviar()

@pytest.mark.sandbox
@pytest.mark.regression
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.click_boton_id_dinamico()

  # Estamos usando el wait_for_element para esperar que el elemento sea visible
  elemento_texto_oculto = sandbox_page.wait_for_element(sandbox_page.HIDDEN_TEXT_LABEL)

  # Creamos la variable con el texto esperado y hacemos el assertion
  texto_esperado = ("OMG, aparezco después de 3 segundos de haber hecho click en el botón")
  assert(texto_esperado in elemento_texto_oculto.text), "El texto esperado no coincide con el texto encontrado"

@pytest.mark.sandbox
@pytest.mark.regression
def test_boton_id_dinamico_cambia_color_al_hacer_over(sandbox_page):
  sandbox_page.navigate_sandbox()
  boton_id_dinamico = sandbox_page.wait_for_element(sandbox_page.DYNAMIC_ID_BUTTON)

  # Obtenemos el color del boton ANTES DE HACER OVER
  color_before_hover = boton_id_dinamico.value_of_css_property("background-color")

  # Usamos el metodo hover_over_element de BasePage para simular el hover
  sandbox_page.hover_over_dynamic_id_button()

  # Obtener el color despues del hover
  color_after_over = boton_id_dinamico.value_of_css_property("background-color")

  # Validar con un assertion que efectivamente son distintos valores antes y despues del hover
  assert (color_before_hover != color_after_over), "El color sigue siendo el mismo"

@pytest.mark.sandbox
def test_elegir_checkbox(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.select_checkbox("Hamburguesa")

@pytest.mark.sandbox
def test_elegir_radio_button(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.select_radio_button('Si')

@pytest.mark.sandbox
def test_elegir_deporte_del_dropdown(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.select_deporte('Tennis')

@allure.title("Las opciones de los checkboxes son las esperadas")
@allure.epic("Interfaz Web")
@allure.feature("Checkboxes")
@allure.story("Comportamiento Checkboxes")
@allure.issue("IS-452")
@allure.testcase("CASE 2")
@allure.severity(allure.severity_level.NORMAL)
@allure.link("https://github.com/TheFreeRangeTester/sandbox-automation-testing/issues/5")
@pytest.mark.new
@pytest.mark.sandbox
def test_deporte_dropdown_options(sandbox_page):
  with allure.step("Dado que navego al sandbox de Free Range Tester"):
    sandbox_page.navigate_sandbox()
  with allure.step("Cuando obtengo todos los elementos del dropdown"):
    options = sandbox_page.get_deporte_dropdown_options()
    expected_options = ["Seleccioná un deporte", "Fútbol", "Tennis", "Basketball"] # Seleccioná
  with allure.step("Puedo validar que efectivamente, todas las opciones del dropdown son correctas y esperadas"):
    assert all(
      option in options for option in expected_options
    ), "No todas las opciones esperadas estan presentes"

@pytest.mark.sandbox
def test_popup_title(sandbox_page):
  sandbox_page.navigate_sandbox()
  sandbox_page.click_button_popup()
  popup_title_text = sandbox_page.get_popup_title_text()
  expected_text = "Popup de ejemplo"

  assert (
    popup_title_text == expected_text
  ), f"El texto del popup es incorrecto, se obtuvo '{popup_title_text}' en su lugar."

@pytest.mark.sandbox
def test_valor_celda_post_recarga(sandbox_page):
  sandbox_page.navigate_sandbox()
  valor_inicial = sandbox_page.get_cell_value(2, 3)
  sandbox_page.reload_page()
  valor_post_recarga = sandbox_page.get_cell_value(2, 3)

  assert (
    valor_inicial != valor_post_recarga
  ), f"El valor de la celda no cambio despues de la recarga, aun es '{valor_inicial}'."


@allure.title("El valor de las celdas NO cambia cuando hay una recarga de la pagina para la tabla estatica")
@allure.epic("Interfaz Web")
@allure.feature("Tabla Estatica")
@allure.story("Comportamiento Celdas")
@allure.issue("IS-102")
@allure.testcase("CASE 1")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://github.com/TheFreeRangeTester/sandbox-automation-testing/issues/5")
@pytest.mark.new
def test_valor_celda_post_recarga(sandbox_page):
  with allure.step("Dado que navego al sandbox de Free Range Tester y tomo como referencia una celda de la tabla estatica"):
    sandbox_page.navigate_sandbox()
    valor_inicial = sandbox_page.get_cell_value_static(2, 3)
  with allure.step("Cuando hago una recarga de la pagina y tomo el valor de la misma celda"):
    sandbox_page.reload_page()
    valor_post_recarga = sandbox_page.get_cell_value_static(2, 3)
  with allure.step("Puedo verificar que el valor, efectivamente, NO se modifico con la recarga de la pagina"):
    assert (
      valor_inicial == valor_post_recarga
    ), f"El valor de la celda no cambio despues de la recarga, aun es '{valor_inicial}'."
