
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # Importar By desde selenium.webdriver.common.by
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get('https://www.google.com/')
    search_box = browser.find_element(By.NAME, 'q')  # Utilizar find_element con By.NAME
    search_box.send_keys('pruebas automatizadas con DevOps')
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Esperar 5 segundos para ver los resultados
    assert 'pruebas automatizadas con DevOps' in browser.title

