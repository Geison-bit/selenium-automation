
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Asegrate de que ChromeDriver est en tu PATH
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element("name", "q")
    search_box.send_keys("Selenium testing with Python")
    search_box.send_keys(Keys.RETURN)
    assert "Selenium testing with Python" in browser.title
