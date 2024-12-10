import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestDemoQAElements:
    @pytest.fixture
    def driver(self):
        """Inicjalizacja przeglądarki Chrome"""
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://demoqa.com/elements")
        yield driver
        driver.quit()

    def test_text_box_valid_input(self, driver):
        """Test poprawnego wypełnienia Text Box"""
        driver.find_element(By.XPATH, "//span[text()='Text Box']").click()

        # Wprowadzenie danych
        driver.find_element(By.ID, "userName").send_keys("Jan Kowalski")
        driver.find_element(By.ID, "userEmail").send_keys("jan.kowalski@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("ul. Testowa 123")
        driver.find_element(By.ID, "permanentAddress").send_keys("ul. Główna 456")

        driver.find_element(By.ID, "submit").click()

        # Weryfikacja wyświetlonych danych
        output_name = driver.find_element(By.ID, "name").text
        output_email = driver.find_element(By.ID, "email").text
        output_current_address = driver.find_element(By.ID, "currentAddress").text
        output_permanent_address = driver.find_element(By.ID, "permanentAddress").text

        assert "Jan Kowalski" in output_name
        assert "jan.kowalski@example.com" in output_email

    def test_text_box_invalid_email(self, driver):
        """Test wprowadzenia nieprawidłowego adresu email"""
        driver.find_element(By.XPATH, "//span[text()='Text Box']").click()

        driver.find_element(By.ID, "userEmail").send_keys("nieprawidłowy-email")
        driver.find_element(By.ID, "submit").click()

        # Sprawdzenie, czy pole email jest oznaczone jako błędne
        email_field = driver.find_element(By.ID, "userEmail")
        assert "field-error" in email_field.get_attribute("class")

    def test_checkbox_expand_and_select(self, driver):
        """Test rozwijania i zaznaczania checkboxów"""
        driver.find_element(By.XPATH, "//span[text()='Check Box']").click()

        # Rozwinięcie głównego folderu
        driver.find_element(By.CLASS_NAME, "rct-collapse-btn").click()

        # Zaznaczenie Commands
        commands_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-commands']")
        commands_checkbox.click()

        # Weryfikacja zaznaczenia
        result_text = driver.find_element(By.ID, "result").text
        assert "commands" in result_text.lower()

    def test_checkbox_select_all_subitems(self, driver):
        """Test zaznaczenia wszystkich podelementów"""
        driver.find_element(By.XPATH, "//span[text()='Check Box']").click()

        # Rozwinięcie głównego folderu
        driver.find_element(By.CLASS_NAME, "rct-expand-all").click()

        # Zaznaczenie Home
        home_checkbox = driver.find_element(By.XPATH, "//label[@for='tree-node-home']")
        home_checkbox.click()

        # Weryfikacja zaznaczenia
        result_text = driver.find_element(By.ID, "result").text
        assert all(item in result_text.lower() for item in ['desktop', 'documents', 'workspace', 'office'])


if __name__ == "__main__":
    pytest.main([__file__])
    # py.test.exe .\test.py