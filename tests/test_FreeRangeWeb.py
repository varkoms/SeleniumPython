import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"""
Los Markers son como "tags"
o etiquetas, que sirven para agrupar
los casos de prueba
"""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def test_navegacion_free_range_web():
  driver.get("https://www.freerangetesters.com")
  driver.find_element(By.XPATH, "(//a[normalize-space()='Cursos' and @href])[1]").click()