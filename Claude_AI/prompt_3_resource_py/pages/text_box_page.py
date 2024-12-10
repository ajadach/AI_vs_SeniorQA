from pages.base_page import BasePage
from locators.text_box_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def navigate_to(self):
        self.click_element(TextBoxLocators.MENU)

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.input_text(TextBoxLocators.FULL_NAME_INPUT, full_name)
        self.input_text(TextBoxLocators.EMAIL_INPUT, email)
        self.input_text(TextBoxLocators.CURRENT_ADDRESS_INPUT, current_address)
        self.input_text(TextBoxLocators.PERMANENT_ADDRESS_INPUT, permanent_address)
        self.click_element(TextBoxLocators.SUBMIT_BUTTON)

    def get_output_name(self):
        return self.get_text(TextBoxLocators.OUTPUT_NAME)