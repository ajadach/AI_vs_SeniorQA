from locators.check_box_locators import CheckBoxLocators
from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    def create(self, item_name):
        self.click(CheckBoxLocators.EXPAND_ALL)
        self.click(CheckBoxLocators.CHECKBOX_ITEM.format(item_name))

    def read(self):
        return [item.text for item in self.driver.find_elements_by_xpath(CheckBoxLocators.CHECKED_ITEMS)]

    def update(self, item_name):
        self.click(CheckBoxLocators.TOGGLE_ITEM.format(item_name))

    def delete(self, item_name):
        self.click(CheckBoxLocators.CHECKBOX_ITEM.format(item_name))
