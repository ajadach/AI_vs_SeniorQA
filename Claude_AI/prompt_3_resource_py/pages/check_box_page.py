from pages.base_page import BasePage
from locators.check_box_locators import CheckBoxLocators

class CheckBoxPage(BasePage):
    def navigate_to(self):
        self.click_element(CheckBoxLocators.MENU)

    def expand_home_directory(self):
        self.click_element(CheckBoxLocators.HOME_EXPAND_BTN)

    def select_home_checkbox(self):
        self.click_element(CheckBoxLocators.HOME_CHECKBOX)

    def get_result_text(self):
        return self.get_text(CheckBoxLocators.RESULT_TEXT)
