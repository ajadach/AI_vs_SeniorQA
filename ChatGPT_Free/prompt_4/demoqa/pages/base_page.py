# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def open_url(self, url):
#         """Otwiera URL."""
#         self.driver.get(url)
#
#     def click_element(self, locator):
#         """Kliknięcie elementu."""
#         element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
#         element.click()
#
#     def enter_text(self, locator, text):
#         """Wprowadzenie tekstu."""
#         element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
#         element.clear()
#         element.send_keys(text)
#
#     def get_element_text(self, locator):
#         """Pobiera tekst elementu."""
#         element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
#         return element.text
#
#     def get_dynamic_locator(self, template, *args):
#         """Zwraca dynamicznie wygenerowany lokator."""
#         return template.format(*args)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        """Otwiera stronę o podanym URL."""
        self.driver.get(url)

    def find_element(self, locator):
        """Znajduje pojedynczy element."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """Kliknięcie w element."""
        element = self.find_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """Wpisuje tekst do pola."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    # added

    def get_element_text(self, locator):
        """Pobiera tekst elementu."""
        element = self.find_element(locator)
        return element.text

    def get_dynamic_locator(self, template, *args):
        """Zwraca dynamicznie wygenerowany lokator."""
        return template.format(*args)
