from pages.base_page import BasePage
from locators.elements_locators import WebTablesLocators

class WebTablesPage(BasePage):
    def create_record(self, first_name, last_name, email, age, salary, department):
        self.click_element(WebTablesLocators.ADD_BUTTON)
        self.input_text(WebTablesLocators.FIRST_NAME_INPUT, first_name)
        self.input_text(WebTablesLocators.LAST_NAME_INPUT, last_name)
        self.input_text(WebTablesLocators.EMAIL_INPUT, email)
        self.input_text(WebTablesLocators.AGE_INPUT, age)
        self.input_text(WebTablesLocators.SALARY_INPUT, salary)
        self.input_text(WebTablesLocators.DEPARTMENT_INPUT, department)
        self.click_element(WebTablesLocators.SUBMIT_FORM)

    def read_record(self, search_term):
        self.input_text(WebTablesLocators.SEARCH_BOX, search_term)
        return self.driver.page_source

    # wow używa search'a w tabeli!!
    def update_record(self, search_term, **updated_fields):
        self.input_text(WebTablesLocators.SEARCH_BOX, search_term)
        self.click_element(WebTablesLocators.EDIT_RECORD)
        for field, value in updated_fields.items():
            if field == "first_name":
                self.input_text(WebTablesLocators.FIRST_NAME_INPUT, value)
            elif field == "last_name":
                self.input_text(WebTablesLocators.LAST_NAME_INPUT, value)
            # ... similar for other fields
        self.click_element(WebTablesLocators.SUBMIT_FORM)

    def delete_record(self, search_term):
        self.input_text(WebTablesLocators.SEARCH_BOX, search_term)
        self.click_element(WebTablesLocators.DELETE_RECORD)