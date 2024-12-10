from locators.web_tables_locators import WebTablesLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class WebTablesPage(BasePage):
    def add_new_record(self, first_name, last_name, email, age, salary, department):
        self.click(WebTablesLocators.ADD_BUTTON)
        self.send_keys(WebTablesLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(WebTablesLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(WebTablesLocators.EMAIL_INPUT, email)
        self.send_keys(WebTablesLocators.AGE_INPUT, age)
        self.send_keys(WebTablesLocators.SALARY_INPUT, salary)
        self.send_keys(WebTablesLocators.DEPARTMENT_INPUT, department)
        self.click(WebTablesLocators.SUBMIT_BUTTON)

    def edit_record(self, record_index, **kwargs):
        # AI_mistake: missing import By
        edit_buttons = self.driver.find_elements(By.XPATH, WebTablesLocators.EDIT_BUTTONS)
        edit_buttons[record_index].click()

        for field, value in kwargs.items():
            if field == 'first_name':
                self.send_keys(WebTablesLocators.FIRST_NAME_INPUT, value)
            elif field == 'last_name':
                self.send_keys(WebTablesLocators.LAST_NAME_INPUT, value)
            # Dodaj pozostałe pola...

        self.click(WebTablesLocators.SUBMIT_BUTTON)

    def delete_record(self, record_index):
        delete_buttons = self.driver.find_elements(By.XPATH, WebTablesLocators.DELETE_BUTTONS)
        delete_buttons[record_index].click()