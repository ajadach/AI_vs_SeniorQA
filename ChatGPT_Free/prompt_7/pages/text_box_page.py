from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from locators.text_box_locators import TextBoxLocators

class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def create(self, data: list):
        """
        Wypełnia formularz Text Box na podstawie listy [parametr, wartość].
        """
        mapping = {
            'Full Name': TextBoxLocators.FULL_NAME,
            'Email': TextBoxLocators.EMAIL,
            'Current Address': TextBoxLocators.CURRENT_ADDRESS,
            'Permanent Address': TextBoxLocators.PERMANENT_ADDRESS
        }
        for param, value in data:
            if param in mapping:
                element = self.driver.find_element(By.XPATH, mapping[param])
                element.clear()
                element.send_keys(value)

        # Kliknięcie przycisku Submit
        self.driver.find_element(By.XPATH, TextBoxLocators.SUBMIT_BUTTON).click()

    def read(self) -> dict:
        """
        Pobiera wartości wyświetlane na UI i zwraca je jako słownik.
        """
        output_mapping = {
            'Full Name': TextBoxLocators.OUTPUT_FULL_NAME,
            'Email': TextBoxLocators.OUTPUT_EMAIL,
            'Current Address': TextBoxLocators.OUTPUT_CURRENT_ADDRESS,
            'Permanent Address': TextBoxLocators.OUTPUT_PERMANENT_ADDRESS
        }
        result = {}

        for key, locator in output_mapping.items():
            element = self.driver.find_element(By.XPATH, locator)
            result[key] = element.get_attribute("innerHTML").split(":")[1].strip() if element else None

        return result

    def update(self, data: list):
        """
        Aktualizuje wartości formularza, nadpisując istniejące dane.
        """
        self.create(data)

    def delete(self):
        """
        Czyści wszystkie pola w formularzu.
        """
        self.create([
            ['Full Name', ''],
            ['Email', ''],
            ['Current Address', ''],
            ['Permanent Address', '']
        ])
