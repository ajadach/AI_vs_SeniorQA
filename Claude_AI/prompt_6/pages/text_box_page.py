from pages.base_page import BasePage
from locators.elements_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def create_user_data(self, full_name, email, current_address, permanent_address):
        self.input_text(TextBoxLocators.FULL_NAME_INPUT, full_name)
        self.input_text(TextBoxLocators.EMAIL_INPUT, email)
        self.input_text(TextBoxLocators.CURRENT_ADDRESS_INPUT, current_address)
        self.input_text(TextBoxLocators.PERMANENT_ADDRESS_INPUT, permanent_address)
        self.click_element(TextBoxLocators.SUBMIT_BUTTON)

    def read_output_data(self):
        return self.get_text(TextBoxLocators.OUTPUT_DIV)

    def update_user_data(self, new_name, new_email, new_current_address, new_permanent_address):
        self.create_user_data(new_name, new_email, new_current_address, new_permanent_address)

    def delete_user_data(self):
        self.create_user_data("", "", "", "")