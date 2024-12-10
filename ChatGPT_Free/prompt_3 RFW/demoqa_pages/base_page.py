from SeleniumLibrary import SeleniumLibrary

class BasePage(SeleniumLibrary):
    def open_url(self, url):
        """Otwiera podany URL."""
        self.go_to(url)

    def click_element(self, locator):
        """Kliknięcie elementu."""
        self.click_element(locator)

    def enter_text(self, locator, text):
        """Wprowadzenie tekstu do pola."""
        self.input_text(locator, text)

    def get_element_text(self, locator):
        """Pobiera tekst elementu."""
        return self.get_text(locator)
