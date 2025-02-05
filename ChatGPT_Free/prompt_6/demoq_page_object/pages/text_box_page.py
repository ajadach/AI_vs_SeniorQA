from locators.text_box_locators import TextBoxLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def create(self, name, email, current_address, permanent_address):
        self.fill(TextBoxLocators.FULL_NAME, name)
        self.fill(TextBoxLocators.EMAIL, email)
        self.fill(TextBoxLocators.CURRENT_ADDRESS, current_address)
        self.fill(TextBoxLocators.PERMANENT_ADDRESS, permanent_address)
        self.click(TextBoxLocators.SUBMIT_BUTTON)

    def read(self):
        return {
            "name": self.get_text(TextBoxLocators.OUTPUT_NAME),
            "email": self.get_text(TextBoxLocators.OUTPUT_EMAIL)
        }
