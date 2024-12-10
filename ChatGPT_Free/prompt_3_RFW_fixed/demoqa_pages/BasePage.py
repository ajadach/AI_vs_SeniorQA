from instances import SELENIUM
from robot.api.deco import keyword


class BasePage():

    @keyword("Open Browser")
    def open_browser(self, url, browser):
        SELENIUM.open_browser(url=url, browser=browser)

    @keyword("Maximize Browser Window")
    def maximize_browser_window(self):
        SELENIUM.maximize_browser_window()

    @keyword("Close Browser")
    def close_browser(self):
        SELENIUM.close_browser()

    def open_url(self, url):
        """Otwiera podany URL."""
        SELENIUM.go_to(url)

    def element_click(self, locator):
        """Kliknięcie elementu."""
        SELENIUM.click_element(locator)

    def enter_text(self, locator, text):
        """Wprowadzenie tekstu do pola."""
        SELENIUM.input_text(locator, text)

    def get_element_text(self, locator):
        """Pobiera tekst elementu."""
        return SELENIUM.get_text(locator)
