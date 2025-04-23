from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.text_box_locators import TextBoxLocators


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def read_all_params(self):
        output_data = {}

        try:
            output_name = self.wait.until(
                EC.presence_of_element_located((By.XPATH, TextBoxLocators.OUTPUT_NAME))
            ).text
            output_data['name'] = output_name.split(':')[1].strip()
        except:
            output_data['name'] = None

        try:
            output_email = self.driver.find_element(By.XPATH, TextBoxLocators.OUTPUT_EMAIL).text
            output_data['email'] = output_email.split(':')[1].strip()
        except:
            output_data['email'] = None

        try:
            output_current_address = self.driver.find_element(
                By.XPATH, TextBoxLocators.OUTPUT_CURRENT_ADDRESS).text
            output_data['current_address'] = output_current_address.split(':')[1].strip()
        except:
            output_data['current_address'] = None

        try:
            output_permanent_address = self.driver.find_element(
                By.XPATH, TextBoxLocators.OUTPUT_PERMANENT_ADDRESS).text
            output_data['permanent_address'] = output_permanent_address.split(':')[1].strip()
        except:
            output_data['permanent_address'] = None

        return output_data

    def choose_parameters(self, params_list):
        for param, value in params_list.items():
            if param == 'Full Name':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, TextBoxLocators.FULL_NAME_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Email':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, TextBoxLocators.EMAIL_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Current Address':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, TextBoxLocators.CURRENT_ADDRESS_INPUT)))
                element.clear()
                element.send_keys(value)
            elif param == 'Permanent Address':
                element = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, TextBoxLocators.PERMANENT_ADDRESS_INPUT)))
                element.clear()
                element.send_keys(value)

        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, TextBoxLocators.SUBMIT_BUTTON)))
        submit_button.click()

        return self.read_all_params()