"""
Przykład użycia biblioteki DemoQA Page Object Pattern
"""

from selenium import webdriver
from demoqa_library import MainPage, TextBoxPage, WebTablesPage


def test_text_box():
    driver = webdriver.Chrome()

    try:
        # Inicjalizacja Text Box Page i nawigacja do strony
        text_box_page = TextBoxPage(driver)
        text_box_page.navigate_from_main_page()

        # Ustawienie parametrów
        params = [
            ["Full Name", "Artur Kowalski"],
            ["Email", "artur@example.com"],
            ["Current Address", "ul. Testowa 1, 00-001 Warszawa"],
            ["Permanent Address", "ul. Stała 5, 00-002 Warszawa"]
        ]

        text_box_page.choose_parameters(params)

        # Odczytanie wszystkich danych
        result = text_box_page.read_all_params()
        print("Text Box Result:", result)

    finally:
        driver.quit()


def test_web_tables():
    driver = webdriver.Chrome()

    try:
        # Inicjalizacja Web Tables Page i nawigacja do strony
        web_tables_page = WebTablesPage(driver)
        web_tables_page.navigate_from_main_page()

        # Dodanie nowego rekordu
        params = [
            ["First Name", "Artur"],
            ["Last Name", "Kowalski"],
            ["Email", "artur@example.com"],
            ["Age", "30"],
            ["Salary", "10000"],
            ["Department", "QA"]
        ]

        web_tables_page.choose_parameters(params)

        # Wyszukanie rekordu
        search_results = web_tables_page.search_record("Artur")
        print("Search Results:", search_results)

        # Edycja rekordu
        edit_params = [
            ["Salary", "12000"],
            ["Department", "Automation"]
        ]

        web_tables_page.edit_record(1, edit_params)

        # Odczytanie wszystkich danych po edycji
        result = web_tables_page.read_all_params()
        print("Web Tables Result after edit:", result)

        # Usunięcie rekordu
        web_tables_page.delete_record(1)

    finally:
        driver.quit()


if __name__ == "__main__":
    test_text_box()
    test_web_tables()