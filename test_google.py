
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import logging

logging.basicConfig(level=logging.DEBUG)

def test_google_search():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")  # Ejecucin sin cabeza
    
    # Ruta al chromedriver.exe
    driver_path = 'D:/Disco Edinson/Downloads/chromedriver-win64/chromedriver.exe'
    
    service = Service(driver_path)
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logging.debug("ChromeDriver started successfully.")
    
    driver.get("http://www.google.com")
    assert "Google" in driver.title
    driver.quit()

