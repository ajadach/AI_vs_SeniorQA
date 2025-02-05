from pages.base_page import BasePage
from locators.elements_locators import CheckBoxLocators

class CheckBoxPage(BasePage):
    def create_checkbox_selection(self, checkbox_xpath):
        self.click_element(CheckBoxLocators.EXPAND_ALL)
        self.click_element(checkbox_xpath)

    def read_checkbox_result(self):
        return self.get_text(CheckBoxLocators.RESULT_TEXT)

    def update_checkbox_selection(self, old_checkbox_xpath, new_checkbox_xpath):
        self.click_element(old_checkbox_xpath)
        self.click_element(new_checkbox_xpath)

    def delete_checkbox_selection(self, checkbox_xpath):
        if self.find_element(checkbox_xpath).is_selected():
            self.click_element(checkbox_xpath)
