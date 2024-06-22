
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging
import os

logging.basicConfig(level=logging.DEBUG)

def test_localhost_login():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    # Eliminar el modo headless para que el navegador sea visible
    # chrome_options.add_argument("--headless")

    # Obtener la ruta actual para asegurarse de la ubicación
    current_dir = os.getcwd()
    logging.debug(f"Current directory: {current_dir}")

    # Ruta al chromedriver.exe, usando ruta relativa desde el directorio principal del proyecto
    driver_path = './drivers/chromedriver.exe'
    logging.debug(f"Chromedriver path: {driver_path}")

    service = Service(driver_path)
    
    driver = webdriver.Chrome(service=service, options=chrome_options)
    logging.debug("ChromeDriver started successfully.")
    
    # Abre la URL local
    driver.get("http://localhost:8080/login/index.html")
    
    # Mantener el navegador abierto hasta que el usuario lo cierre manualmente
    input("Presiona Enter para cerrar el navegador...")
    
    driver.quit()


