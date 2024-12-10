from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        """Otwiera URL."""
        self.driver.get(url)

    def click_element(self, locator):
        """Kliknięcie elementu."""
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
        element.click()

    def enter_text(self, locator, text):
        """Wprowadzenie tekstu."""
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Pobiera tekst elementu."""
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element.text

    def get_dynamic_locator(self, template, *args):
        """Zwraca dynamicznie wygenerowany lokator."""
        return template.format(*args)
