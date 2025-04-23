from selenium.webdriver.common.by import By
from locators.text_box_locators import TextBoxLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def navigate_to_page(self):
        self.driver.get('https://demoqa.com/text-box')

    def read_all_params(self):
        params = {
            'Full Name': self.get_text(By.XPATH, TextBoxLocators.FULL_NAME_INPUT),
            'Email': self.get_text(By.XPATH, TextBoxLocators.EMAIL_INPUT),
            'Current Address': self.get_text(By.XPATH, TextBoxLocators.CURRENT_ADDRESS_INPUT),
            'Permanent Address': self.get_text(By.XPATH, TextBoxLocators.PERMANENT_ADDRESS_INPUT)
        }
        return params

    def choose_parameters(self, params_list):
        for param in params_list:
            if param == 'Full Name':
                self.send_keys(By.XPATH, TextBoxLocators.FULL_NAME_INPUT, params_list[param])
            elif param == 'Email':
                self.send_keys(By.XPATH, TextBoxLocators.EMAIL_INPUT, params_list[param])
            elif param == 'Current Address':
                self.send_keys(By.XPATH, TextBoxLocators.CURRENT_ADDRESS_INPUT, params_list[param])
            elif param == 'Permanent Address':
                self.send_keys(By.XPATH, TextBoxLocators.PERMANENT_ADDRESS_INPUT, params_list[param])
        self.click(By.XPATH, TextBoxLocators.SUBMIT_BUTTON)
