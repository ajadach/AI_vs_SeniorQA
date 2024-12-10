from demoqa_page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    TEXT_BOX_MENU = (By.ID, "item-0")
    FULL_NAME_FIELD = (By.ID, "userName")
    EMAIL_FIELD = (By.ID, "userEmail")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_TEXT = (By.ID, "output")

    def open_text_box(self):
        """Przejście do Text Box."""
        self.click_element(self.TEXT_BOX_MENU)

    def fill_text_box(self, name, email):
        """Wypełnienie formularza Text Box."""
        self.enter_text(self.FULL_NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.click_element(self.SUBMIT_BUTTON)

    def get_output_text(self):
        """Pobiera tekst z sekcji wyników."""
        return self.find_element(self.OUTPUT_TEXT).text
