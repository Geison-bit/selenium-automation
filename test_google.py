
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import platform

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # Opcional: para ejecucin sin cabeza
    chrome_options.add_argument("--headless")

    # Ajustar la ruta segn el sistema operativo
    driver_path = 'D:/Disco Edinson/Downloads/chromedriver-win64/chromedriver.exe'

    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get('https://www.google.com/')
    search_box = browser.find_element(By.NAME, 'q')
    search_box.send_keys('pruebas automatizadas con devops')
    search_box.submit()
    assert 'pruebas automatizadas con devops' in browser.title

