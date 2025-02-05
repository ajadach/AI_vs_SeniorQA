import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    yield driver
    driver.quit()
