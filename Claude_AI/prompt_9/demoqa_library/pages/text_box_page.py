"""Klasa reprezentująca podstronę Text Box"""

import time
from ..base_page import BasePage
from ..locators.text_box_locators import TextBoxLocators

class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/text-box"

    def navigate_to_page(self):
        """Bezpośrednia nawigacja do Text Box"""
        self.visit(self.url)
        return self

    def navigate_from_main_page(self):
        """Nawigacja od strony głównej do Text Box"""
        from .main_page import MainPage
        main_page = MainPage(self.driver)
        main_page.navigate_to_page()
        elements_page = main_page.navigate_to_elements()
        return elements_page.navigate_to_text_box()

    def read_all_params(self):
        """Odczytaj wszystkie dane, które są wyświetlone dla użytkownika"""
        result = {}

        # Sprawdź, czy output box jest widoczny
        if self.is_displayed(TextBoxLocators.OUTPUT_BOX):
            if self.is_displayed(TextBoxLocators.OUTPUT_NAME):
                name_text = self.get_text(TextBoxLocators.OUTPUT_NAME)
                result["Full Name"] = name_text.replace("Name:", "").strip() if name_text else ""

            if self.is_displayed(TextBoxLocators.OUTPUT_EMAIL):
                email_text = self.get_text(TextBoxLocators.OUTPUT_EMAIL)
                result["Email"] = email_text.replace("Email:", "").strip() if email_text else ""

            if self.is_displayed(TextBoxLocators.OUTPUT_CURRENT_ADDRESS):
                curr_addr_text = self.get_text(TextBoxLocators.OUTPUT_CURRENT_ADDRESS)
                result["Current Address"] = curr_addr_text.replace("Current Address :", "").strip() if curr_addr_text else ""

            if self.is_displayed(TextBoxLocators.OUTPUT_PERMANENT_ADDRESS):
                perm_addr_text = self.get_text(TextBoxLocators.OUTPUT_PERMANENT_ADDRESS)
                result["Permanent Address"] = perm_addr_text.replace("Permananet Address :", "").strip() if perm_addr_text else ""

        return result

    def choose_parameters(self, params_list):
        """
        Ustawia parametry na podstawie listy par [parametr, wartość]

        Args:
            params_list: Lista par [parametr, wartość], np. [['Full Name', 'Artur'], ['Email', 'artur@example.com']]

        Returns:
            dict: Słownik z ustawionymi parametrami
        """
        param_dict = {}

        for param_pair in params_list:
            if len(param_pair) != 2:
                continue

            param, value = param_pair
            param_dict[param] = value

            if param == "Full Name":
                self.input_text(TextBoxLocators.FULL_NAME_INPUT, value)
            elif param == "Email":
                self.input_text(TextBoxLocators.EMAIL_INPUT, value)
            elif param == "Current Address":
                self.input_text(TextBoxLocators.CURRENT_ADDRESS_INPUT, value)
            elif param == "Permanent Address":
                self.input_text(TextBoxLocators.PERMANENT_ADDRESS_INPUT, value)

        # Kliknij przycisk Submit
        self.click(TextBoxLocators.SUBMIT_BUTTON)

        # Daj czas na załadowanie wyników
        time.sleep(1)

        return param_dict