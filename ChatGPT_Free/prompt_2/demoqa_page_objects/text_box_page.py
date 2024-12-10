from demoqa_page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class TextBoxPage(BasePage):
    FULL_NAME_FIELD = (By.ID, "userName")
    EMAIL_FIELD = (By.ID, "userEmail")
    CURRENT_ADDRESS_FIELD = (By.ID, "currentAddress")
    PERMANENT_ADDRESS_FIELD = (By.ID, "permanentAddress")
    SUBMIT_BUTTON = (By.ID, "submit")
    OUTPUT_SECTION = (By.ID, "output")

    def fill_form(self, name, email, current_address, permanent_address):
        """Wypełnia formularz Text Box."""
        self.enter_text(self.FULL_NAME_FIELD, name)
        self.enter_text(self.EMAIL_FIELD, email)
        self.enter_text(self.CURRENT_ADDRESS_FIELD, current_address)
        self.enter_text(self.PERMANENT_ADDRESS_FIELD, permanent_address)
        self.click_element(self.SUBMIT_BUTTON)

    def get_output_text(self):
        """Zwraca zawartość sekcji wyników."""
        return self.find_element(self.OUTPUT_SECTION).text
