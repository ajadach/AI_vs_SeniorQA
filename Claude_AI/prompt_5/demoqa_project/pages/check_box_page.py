from locators.check_box_locators import CheckBoxLocators
from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    def expand_home(self):
        self.click(CheckBoxLocators.HOME_EXPAND_BTN)

    def select_home_checkbox(self):
        self.click(CheckBoxLocators.HOME_CHECKBOX)

    def get_result_text(self):
        return self.find_element(CheckBoxLocators.RESULT_TEXT).text