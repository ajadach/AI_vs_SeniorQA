from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.web_tables_locators import WebTablesLocators


class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def read_all_params(self):
        table_data = []
        rows = self.driver.find_elements(By.XPATH, WebTablesLocators.TABLE_ROWS)

        for row in rows:
            cells = row.find_elements(By.XPATH, WebTablesLocators.ROW_DATA)
            if len(cells) >= 6:  # Sprawdzamy, czy wiersz zawiera dane (a nie jest pusty)
                row_data = {
                    'first_name': cells[0].text,
                    'last_name': cells[1].text,
                    'age': cells[2].text,
                    'email': cells[3].text,
                    'salary': cells[4].text,
                    'department': cells[5].text,
                }
                table_data.append(row_data)

        return {'table_data': table_data}

    def choose_parameters(self, params_list):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, WebTablesLocators.ADD_BUTTON)))
        add_button.click()

        for param, value in params_list.items():
            if param == 'First Name':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.FIRST_NAME_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Last Name':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.LAST_NAME_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Email':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.EMAIL_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Age':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.AGE_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Salary':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.SALARY_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Department':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, WebTablesLocators.DEPARTMENT_INPUT)))
                element.clear()
                element.send_keys(value)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, WebTablesLocators.SUBMIT_BUTTON)))
        submit_button.click()

        return self.read_all_params()