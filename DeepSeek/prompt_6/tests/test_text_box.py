import pytest
from selenium import webdriver
from pages.text_box_page import TextBoxPage
from locators.text_box_locators import TextBoxLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    yield driver
    driver.quit()

def test_create_user(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.create_user("John Doe", "john.doe@example.com", "123 Main St", "456 Secondary St")
    user_data = text_box_page.read_user_data()
    assert "John Doe" in user_data["name"]
    assert "john.doe@example.com" in user_data["email"]
    assert "123 Main St" in user_data["current_address"]
    assert "456 Secondary St" in user_data["permanent_address"]