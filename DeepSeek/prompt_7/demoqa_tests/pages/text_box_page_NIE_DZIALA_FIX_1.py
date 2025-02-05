from .base_page import BasePage
from locators.text_box_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def create(self, data):
        """
        Tworzy rekord w Text Box na podstawie listy parametrów.
        :param data: Lista w formacie [nazwa_parametru, wartość], np. ['Full Name', 'Artur']
        """
        for param, value in data.items():
            if param == "Full Name":
                self.send_keys(TextBoxLocators.FULL_NAME_INPUT, value)
            elif param == "Email":
                self.send_keys(TextBoxLocators.EMAIL_INPUT, value)
            elif param == "Current Address":
                self.send_keys(TextBoxLocators.CURRENT_ADDRESS_INPUT, value)
            elif param == "Permanent Address":
                self.send_keys(TextBoxLocators.PERMANENT_ADDRESS_INPUT, value)
        self.click(TextBoxLocators.SUBMIT_BUTTON)

    def read(self):
        """
        Odczytuje dane z UI i zwraca je w postaci słownika.
        """
        output_data = {
            "Name": self.get_inner_html(TextBoxLocators.OUTPUT_NAME).replace("Name:", "").strip(),
            "Email": self.get_inner_html(TextBoxLocators.OUTPUT_EMAIL).replace("Email:", "").strip(),
            "Current Address": self.get_inner_html(TextBoxLocators.OUTPUT_CURRENT_ADDRESS).replace("Current Address :", "").strip(),
            "Permanent Address": self.get_inner_html(TextBoxLocators.OUTPUT_PERMANENT_ADDRESS).replace("Permanent Address :", "").strip(),
        }
        return output_data

    def update(self, data):
        """
        Aktualizuje istniejący rekord w Text Box.
        :param data: Lista w formacie [nazwa_parametru, wartość], np. ['Full Name', 'Nowe Imię']
        """
        self.create(data)

    def delete(self):
        """
        Czyści wszystkie pola w Text Box.
        """
        self.send_keys(TextBoxLocators.FULL_NAME_INPUT, "")
        self.send_keys(TextBoxLocators.EMAIL_INPUT, "")
        self.send_keys(TextBoxLocators.CURRENT_ADDRESS_INPUT, "")
        self.send_keys(TextBoxLocators.PERMANENT_ADDRESS_INPUT, "")