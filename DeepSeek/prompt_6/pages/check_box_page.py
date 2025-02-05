from .base_page import BasePage
from locators.check_box_locators import CheckBoxLocators

class CheckBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def expand_all(self):
        self.click(CheckBoxLocators.EXPAND_ALL_BUTTON)

    def collapse_all(self):
        self.click(CheckBoxLocators.COLLAPSE_ALL_BUTTON)

    def select_checkbox(self, checkbox_locator):
        self.click(checkbox_locator)

    def get_output_result(self):
        return self.get_text(CheckBoxLocators.OUTPUT_RESULT)