from demoqa.pages.base_page import BasePage
from demoqa.locators.web_tables_locators import WebTablesLocators

class WebTablesPage(BasePage):
    def delete_row(self, name):
        """Usuwa wiersz na podstawie imienia."""
        delete_button = self.get_dynamic_locator(WebTablesLocators.DELETE_BUTTON, name)
        self.click_element(delete_button)

    def edit_row(self, name, new_data):
        """Edytuje wiersz na podstawie imienia."""
        edit_button = self.get_dynamic_locator(WebTablesLocators.EDIT_BUTTON, name)
        self.click_element(edit_button)

        # Wypełnianie formularza
        self.enter_text(WebTablesLocators.FIRST_NAME_FIELD, new_data["first_name"])
        self.enter_text(WebTablesLocators.LAST_NAME_FIELD, new_data["last_name"])
        self.enter_text(WebTablesLocators.EMAIL_FIELD, new_data["email"])
        self.enter_text(WebTablesLocators.AGE_FIELD, new_data["age"])
        self.enter_text(WebTablesLocators.SALARY_FIELD, new_data["salary"])
        self.enter_text(WebTablesLocators.DEPARTMENT_FIELD, new_data["department"])
        self.click_element(WebTablesLocators.SUBMIT_BUTTON)

    def get_rows_count(self):
        """Zwraca liczbę wierszy w tabeli."""
        rows = self.driver.find_elements_by_css_selector(WebTablesLocators.ROWS)
        return len(rows)
