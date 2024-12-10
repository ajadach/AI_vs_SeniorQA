from demoqa_pages.base_page import BasePage

class TextBoxPage(BasePage):
    FULL_NAME_FIELD = "id:userName"
    EMAIL_FIELD = "id:userEmail"
    CURRENT_ADDRESS_FIELD = "id:currentAddress"
    PERMANENT_ADDRESS_FIELD = "id:permanentAddress"
    SUBMIT_BUTTON = "id:submit"
    OUTPUT_SECTION = "id:output"

    def fill_text_box_form(self, name, email, current_address, permanent_address):
        """Wypełnia formularz Text Box."""
        self.enter_text(self.FULL_NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.CURRENT_ADDRESS_FIELD, current_address)
        self.enter_text(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click_element(self.SUBMIT_BUTTON)

    def get_output_text(self):
        """Pobiera tekst z wyników."""
        return self.get_element_text(self.OUTPUT_SECTION)
