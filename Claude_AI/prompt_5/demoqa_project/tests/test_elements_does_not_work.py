# tests/test_elements.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.text_box_page import TextBoxPage
from pages.check_box_page import CheckBoxPage
from pages.web_tables_page import WebTablesPage


class TestDemoQAElements:
    @pytest.fixture
    def driver(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://demoqa.com/elements")
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_text_box(self, driver):
        # Nawigacja do Text Box
        driver.find_element_by_xpath("//span[contains(text(), 'Text Box')]").click()

        text_box_page = TextBoxPage(driver)
        text_box_page.fill_form(
            full_name="Jan Kowalski",
            email="jan.kowalski@example.com",
            current_address="ul. Testowa 123",
            permanent_address="ul. Główna 456"
        )

        # Weryfikacja wyniku
        assert "Jan Kowalski" in text_box_page.get_output_name()

    def test_check_box(self, driver):
        # Nawigacja do Check Box
        # AI_mistake: find_element_by_xpath was repalced to find_element in selenium
        driver.find_element_by_xpath("//span[contains(text(), 'Check Box')]").click()

        check_box_page = CheckBoxPage(driver)
        check_box_page.expand_home()
        check_box_page.select_home_checkbox()

        # Weryfikacja zaznaczenia
        result_text = check_box_page.get_result_text()
        assert all(item in result_text.lower() for item in ['desktop', 'documents'])

    def test_web_tables(self, driver):
        # Nawigacja do Web Tables
        driver.find_element_by_xpath("//span[contains(text(), 'Web Tables')]").click()

        web_tables_page = WebTablesPage(driver)

        # Test dodawania nowego rekordu
        web_tables_page.add_new_record(
            first_name="Tomasz",
            last_name="Nowak",
            email="tomasz.nowak@example.com",
            age="30",
            salary="5000",
            department="IT"
        )

        # Test edycji rekordu
        web_tables_page.edit_record(
            record_index=0,
            first_name="Piotr",
            last_name="Kowalczyk"
        )

        # Test usuwania rekordu
        web_tables_page.delete_record(record_index=0)


if __name__ == "__main__":
    pytest.main([__file__])