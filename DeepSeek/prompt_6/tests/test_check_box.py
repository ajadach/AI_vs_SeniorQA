import pytest
from selenium import webdriver
from pages.check_box_page import CheckBoxPage
from locators.check_box_locators import CheckBoxLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/checkbox")
    yield driver
    driver.quit()

def test_select_checkbox(driver):
    check_box_page = CheckBoxPage(driver)
    check_box_page.expand_all()
    check_box_page.select_checkbox(CheckBoxLocators.CHECKBOX_HOME)
    output_result = check_box_page.get_output_result()
    assert "home" in output_result.lower()