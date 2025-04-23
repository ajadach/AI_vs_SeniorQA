from selenium.webdriver.common.by import By
from locators.web_tables_locators import WebTablesLocators
from pages.base_page import BasePage


class WebTablesPage(BasePage):

    def navigate_to_page(self):
        self.driver.get('https://demoqa.com/webtables')

    def read_all_params(self):
        rows = self.find_elements(By.XPATH, WebTablesLocators.TABLE_ROWS)
        table_data = []
        for row in rows:
            row_data = {
                'First Name': row.find_element(By.XPATH, './div[1]').text,
                'Last Name': row.find_element(By.XPATH, './div[2]').text,
                'Age': row.find_element(By.XPATH, './div[3]').text,
                'Salary': row.find_element(By.XPATH, './div[4]').text,
                'Department': row.find_element(By.XPATH, './div[5]').text,
            }
            table_data.append(row_data)
        return table_data

    def choose_parameters(self, params_list):
        self.click(By.XPATH, WebTablesLocators.ADD_BUTTON)
        self.send_keys(By.XPATH, WebTablesLocators.FIRST_NAME_INPUT, params_list.get('First Name'))
        self.send_keys(By.XPATH, WebTablesLocators.LAST_NAME_INPUT, params_list.get('Last Name'))
        self.send_keys(By.XPATH, WebTablesLocators.AGE_INPUT, params_list.get('Age'))
        self.send_keys(By.XPATH, WebTablesLocators.SALARY_INPUT, params_list.get('Salary'))
        self.send_keys(By.XPATH, WebTablesLocators.DEPARTMENT_INPUT, params_list.get('Department'))
        self.click(By.XPATH, WebTablesLocators.SUBMIT_BUTTON)
