import pytest
from selenium import webdriver
from pages.text_box_page import TextBoxPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    yield driver
    driver.quit()

def test_create_and_read_text_box(driver):
    text_box_page = TextBoxPage(driver)

    # Dane do wprowadzenia
    input_data = {
        "Full Name": "Artur",
        "Email": "artur@example.com",
        "Current Address": "123 Main St",
        "Permanent Address": "456 Secondary St"
    }

    # Tworzenie rekordu
    text_box_page.create(input_data)

    # Odczytanie danych z UI
    output_data = text_box_page.read()

    # Sprawdzenie, czy dane się zgadzają
    assert output_data["Name"] == "Artur"
    assert output_data["Email"] == "artur@example.com"
    assert output_data["Current Address"] == "123 Main St"
    assert output_data["Permanent Address"] == "456 Secondary St"

def test_update_text_box(driver):
    text_box_page = TextBoxPage(driver)

    # Dane początkowe
    initial_data = {
        "Full Name": "Artur",
        "Email": "artur@example.com",
        "Current Address": "123 Main St",
        "Permanent Address": "456 Secondary St"
    }

    # Aktualizacja danych
    updated_data = {
        "Full Name": "Jan Kowalski",
        "Email": "jan.kowalski@example.com",
        "Current Address": "789 New St",
        "Permanent Address": "101 Old St"
    }

    # Tworzenie rekordu
    text_box_page.create(initial_data)

    # Aktualizacja rekordu
    text_box_page.update(updated_data)

    # Odczytanie danych z UI
    output_data = text_box_page.read()

    # Sprawdzenie, czy dane zostały zaktualizowane
    assert output_data["Name"] == "Jan Kowalski"
    assert output_data["Email"] == "jan.kowalski@example.com"
    assert output_data["Current Address"] == "789 New St"
    assert output_data["Permanent Address"] == "101 Old St"

def test_delete_text_box(driver):
    text_box_page = TextBoxPage(driver)

    # Dane do wprowadzenia
    input_data = {
        "Full Name": "Artur",
        "Email": "artur@example.com",
        "Current Address": "123 Main St",
        "Permanent Address": "456 Secondary St"
    }

    # Tworzenie rekordu
    text_box_page.create(input_data)

    # Usunięcie rekordu
    text_box_page.delete()

    # Odczytanie danych z UI
    output_data = text_box_page.read()

    # Sprawdzenie, czy dane zostały usunięte
    assert output_data["Name"] == ""
    assert output_data["Email"] == ""
    assert output_data["Current Address"] == ""
    assert output_data["Permanent Address"] == ""