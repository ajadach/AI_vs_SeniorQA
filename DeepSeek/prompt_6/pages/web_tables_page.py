from .base_page import BasePage
from locators.web_tables_locators import WebTablesLocators

class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_record(self, first_name, last_name, email, age, salary, department):
        self.click(WebTablesLocators.ADD_BUTTON)
        self.send_keys(WebTablesLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(WebTablesLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(WebTablesLocators.EMAIL_INPUT, email)
        self.send_keys(WebTablesLocators.AGE_INPUT, age)
        self.send_keys(WebTablesLocators.SALARY_INPUT, salary)
        self.send_keys(WebTablesLocators.DEPARTMENT_INPUT, department)
        self.click(WebTablesLocators.SUBMIT_BUTTON)

    def search_record(self, search_text):
        self.send_keys(WebTablesLocators.SEARCH_BOX, search_text)

    def edit_record(self, new_first_name):
        self.click(WebTablesLocators.EDIT_BUTTON)
        self.send_keys(WebTablesLocators.FIRST_NAME_INPUT, new_first_name)
        self.click(WebTablesLocators.SUBMIT_BUTTON)

    def delete_record(self):
        self.click(WebTablesLocators.DELETE_BUTTON)

    def get_row_data(self):
        return self.get_text(WebTablesLocators.ROW_DATA)