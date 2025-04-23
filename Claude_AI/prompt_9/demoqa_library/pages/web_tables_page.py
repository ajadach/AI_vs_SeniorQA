"""Klasa reprezentująca podstronę Web Tables"""

import time
from selenium.webdriver.common.by import By
from ..base_page import BasePage
from ..locators.web_tables_locators import WebTablesLocators

class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/webtables"

    def navigate_to_page(self):
        """Bezpośrednia nawigacja do Web Tables"""
        self.visit(self.url)
        return self

    def navigate_from_main_page(self):
        """Nawigacja od strony głównej do Web Tables"""
        from .main_page import MainPage
        main_page = MainPage(self.driver)
        main_page.navigate_to_page()
        elements_page = main_page.navigate_to_elements()
        return elements_page.navigate_to_web_tables()

    def read_all_params(self):
        """Odczytaj wszystkie dane z tabeli"""
        result = []
        rows = self.find_elements(WebTablesLocators.TABLE_ROWS)

        for i, row in enumerate(rows):
            cells = row.find_elements(By.XPATH, ".//div[@class='rt-td']")

            # Pomijamy puste wiersze
            if cells and cells[0].text.strip():
                row_data = {
                    "First Name": cells[0].text.strip(),
                    "Last Name": cells[1].text.strip(),
                    "Age": cells[2].text.strip(),
                    "Email": cells[3].text.strip(),
                    "Salary": cells[4].text.strip(),
                    "Department": cells[5].text.strip(),
                    "Row": i + 1  # Indeks wiersza (1-based)
                }
                result.append(row_data)

        return result

    def fill_form(self, params_list):
        """
        Wypełnia formularz na podstawie listy par [parametr, wartość]

        Args:
            params_list: Lista par [parametr, wartość], np. [['First Name', 'Artur'], ['Age', '30']]

        Returns:
            dict: Słownik z ustawionymi parametrami
        """
        param_dict = {}

        for param_pair in params_list:
            if len(param_pair) != 2:
                continue

            param, value = param_pair
            param_dict[param] = value

            if param == "First Name":
                self.input_text(WebTablesLocators.FIRST_NAME_INPUT, value)
            elif param == "Last Name":
                self.input_text(WebTablesLocators.LAST_NAME_INPUT, value)
            elif param == "Email":
                self.input_text(WebTablesLocators.EMAIL_INPUT, value)
            elif param == "Age":
                self.input_text(WebTablesLocators.AGE_INPUT, value)
            elif param == "Salary":
                self.input_text(WebTablesLocators.SALARY_INPUT, value)
            elif param == "Department":
                self.input_text(WebTablesLocators.DEPARTMENT_INPUT, value)

        # Kliknij przycisk Submit
        self.click(WebTablesLocators.SUBMIT_FORM_BUTTON)

        # Daj czas na załadowanie tabeli
        time.sleep(1)

        return param_dict

    def choose_parameters(self, params_list):
        """
        Dodaje nowy rekord do tabeli na podstawie listy par [parametr, wartość]

        Args:
            params_list: Lista par [parametr, wartość], np. [['First Name', 'Artur'], ['Age', '30']]

        Returns:
            dict: Słownik z dodanymi parametrami
        """
        # Kliknij przycisk Add
        self.click(WebTablesLocators.ADD_BUTTON)

        # Wypełnij formularz
        return self.fill_form(params_list)

    def search_record(self, search_text):
        """
        Wyszukuje rekord w tabeli

        Args:
            search_text: Tekst do wyszukania

        Returns:
            list: Lista znalezionych rekordów
        """
        self.input_text(WebTablesLocators.SEARCH_BOX, search_text)
        time.sleep(1)  # Daj czas na filtrowanie
        return self.read_all_params()

    def edit_record(self, row_index, params_list):
        """
        Edytuje rekord o określonym indeksie

        Args:
            row_index: Indeks wiersza (1-based)
            params_list: Lista par [parametr, wartość] do edycji

        Returns:
            dict: Słownik z edytowanymi parametrami
        """
        edit_button_xpath = f"({WebTablesLocators.TABLE_ROWS})[{row_index}]//span[@title='Edit']"
        self.click(edit_button_xpath)

        # Wypełnij formularz
        result = self.fill_form(params_list)
        return result

    def delete_record(self, row_index):
        """
        Usuwa rekord o określonym indeksie

        Args:
            row_index: Indeks wiersza (1-based)

        Returns:
            bool: True jeśli operacja się powiodła
        """
        delete_button_xpath = f"({WebTablesLocators.TABLE_ROWS})[{row_index}]//span[@title='Delete']"
        self.click(delete_button_xpath)
        time.sleep(1)  # Daj czas na usunięcie
        return True