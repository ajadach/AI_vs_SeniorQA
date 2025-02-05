from .base_page import BasePage
from locators.text_box_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create_user(self, full_name, email, current_address, permanent_address):
        self.send_keys(TextBoxLocators.FULL_NAME_INPUT, full_name)
        self.send_keys(TextBoxLocators.EMAIL_INPUT, email)
        self.send_keys(TextBoxLocators.CURRENT_ADDRESS_INPUT, current_address)
        self.send_keys(TextBoxLocators.PERMANENT_ADDRESS_INPUT, permanent_address)
        self.click(TextBoxLocators.SUBMIT_BUTTON)

    def read_user_data(self):
        return {
            "name": self.get_text(TextBoxLocators.OUTPUT_NAME),
            "email": self.get_text(TextBoxLocators.OUTPUT_EMAIL),
            "current_address": self.get_text(TextBoxLocators.OUTPUT_CURRENT_ADDRESS),
            "permanent_address": self.get_text(TextBoxLocators.OUTPUT_PERMANENT_ADDRESS)
        }