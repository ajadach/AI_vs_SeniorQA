import pytest
from selenium import webdriver
from pages.web_tables_page import WebTablesPage
from locators.web_tables_locators import WebTablesLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/webtables")
    yield driver
    driver.quit()

def test_add_record(driver):
    web_tables_page = WebTablesPage(driver)
    web_tables_page.add_record("John", "Doe", "john.doe@example.com", "30", "50000", "IT")
    web_tables_page.search_record("John")
    row_data = web_tables_page.get_row_data()
    assert "John" in row_data
    assert "Doe" in row_data
    assert "john.doe@example.com" in row_data
    assert "30" in row_data
    assert "50000" in row_data
    assert "IT" in row_data

def test_edit_record(driver):
    web_tables_page = WebTablesPage(driver)
    web_tables_page.edit_record("Jane")
    web_tables_page.search_record("Jane")
    row_data = web_tables_page.get_row_data()
    assert "Jane" in row_data

def test_delete_record(driver):
    web_tables_page = WebTablesPage(driver)
    web_tables_page.delete_record()
    row_data = web_tables_page.get_row_data()
    assert "John" not in row_data