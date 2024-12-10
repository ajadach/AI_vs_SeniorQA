from locators.text_box_locators import TextBoxLocators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def fill_form(self, full_name, email, current_address, permanent_address):
        self.send_keys(TextBoxLocators.FULL_NAME_INPUT, full_name)
        self.send_keys(TextBoxLocators.EMAIL_INPUT, email)
        self.send_keys(TextBoxLocators.CURRENT_ADDRESS_INPUT, current_address)
        self.send_keys(TextBoxLocators.PERMANENT_ADDRESS_INPUT, permanent_address)
        self.click(TextBoxLocators.SUBMIT_BUTTON)

    def get_output_name(self):
        return self.find_element(TextBoxLocators.OUTPUT_NAME).text