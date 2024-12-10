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
