from demoqa.pages.base_page import BasePage
from demoqa.locators.text_box_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def fill_text_box_form(self, name, email, current_address, permanent_address):
        """Wypełnia formularz Text Box."""
        self.enter_text(TextBoxLocators.FULL_NAME_FIELD, name)
        self.enter_text(TextBoxLocators.EMAIL_FIELD, email)
        self.enter_text(TextBoxLocators.CURRENT_ADDRESS_FIELD, current_address)
        self.enter_text(TextBoxLocators.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click_element(TextBoxLocators.SUBMIT_BUTTON)

    def get_output_text(self):
        """Pobiera tekst z wyników."""
        return self.get_element_text(TextBoxLocators.OUTPUT_SECTION)
