"""Bazowa klasa dla wszystkich stron"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def visit(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            raise NoSuchElementException(f"Element nie znaleziony: {locator}")

    def find_elements(self, locator):
        try:
            return self.wait.until(EC.presence_of_all_elements_located((By.XPATH, locator)))
        except TimeoutException:
            return []

    def click(self, locator):
        element = self.find_element(locator)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False