from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
  ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")
  DYNAMIC_ID_BUTTON = (By.XPATH, "//button[contains(text(), 'Hacé')]")
  HIDDEN_TEXT_LABEL = (By.XPATH, "//p[contains(text(), 'OMG')]")
  DEPORTE_DROPDOWN = (By.ID, "formBasicSelect")
  MOSTRAR_POPUP_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and text()='Mostrar popup']")
  POPUP_TITLE = (By.ID, "contained-modal-title-vcenter")

  def navigate_sandbox(self):
    self.navigate_to("https://thefreerangetester.github.io/sandbox-automation-testing")

  def click_enviar(self):
    self.click(self.ENVIAR_BUTTON)

  def click_boton_id_dinamico(self):
    self.click(self.DYNAMIC_ID_BUTTON)

  def hover_over_dynamic_id_button(self):
    self.hover_over_element(self.DYNAMIC_ID_BUTTON)

  def select_checkbox(self, label_text):
    assert label_text in ["Pizza", "Hamburguesa", "Pasta", "Helado", "Torta"], "La opcion seleccionada es incorrecta"
    checkbox_locator = (
      By.XPATH,
      f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']"
    )
    self.select_element(checkbox_locator)

  def select_radio_button(self, option):
    assert option in ["Si", "No"], "La opcion tiene que ser Si o No"
    radio_button_locator = (
      By.XPATH,
      f"//label[@class='form-check-label' and contains(text(), '{option}')]"
    )

    self.select_element(radio_button_locator)

  def select_deporte(self, deporte):
    self.select_from_dropdown_by_visible_text(self.DEPORTE_DROPDOWN, deporte)

  def get_deporte_dropdown_options(self):
    return self.get_select_options(self.DEPORTE_DROPDOWN)

  def click_button_popup(self):
    self.hover_over_element(self.MOSTRAR_POPUP_BUTTON)
    self.click(self.MOSTRAR_POPUP_BUTTON)

  def get_popup_title_text(self):
    return self.wait_for_element(self.POPUP_TITLE).text

  def get_cell_value(self, fila, columna):
    celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}]/td[{columna}]"
    celda = self.wait_for_element((By.XPATH, celda_xpath))
    return celda.text if celda else None

  def get_cell_value_static(self, fila, columna):
    celda_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{fila}]/td[{columna}]"
    celda = self.wait_for_element((By.XPATH, celda_xpath))
    return celda.text if celda else None
