from locators.web_tables_locators import WebTablesLocators
from pages.base_page import BasePage

class WebTablesPage(BasePage):
    def create(self):
        self.click(WebTablesLocators.ADD_BUTTON)

    def read(self):
        return [row.text for row in self.driver.find_elements_by_xpath(WebTablesLocators.TABLE_ROWS)]

    def update(self, row_index):
        self.driver.find_elements_by_xpath(WebTablesLocators.EDIT_BUTTON)[row_index].click()

    def delete(self, row_index):
        self.driver.find_elements_by_xpath(WebTablesLocators.DELETE_BUTTON)[row_index].click()
