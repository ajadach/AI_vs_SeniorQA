from selenium.webdriver.common.by import By
import lxml.html
from locators.text_box_locators import TEXT_BOX_LOCATORS


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.XPATH, "//*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Text Box']").click()

    def read_all_params(self):
        inner_html = self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['full_name_text']).get_attribute('innerHTML')
        root = lxml.html.fromstring(inner_html)
        divs = root.xpath(".//div")

        params = {}
        for div in divs:
            text = div.text.strip() if div.text else ''
            params['full_name'] = text  # Assuming there is only one value to extract here
        return params

    def choose_parameters(self, parameters):
        if 'Full Name' in parameters:
            self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['full_name_input']).send_keys(parameters['Full Name'])
        if 'Email' in parameters:
            self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['email_input']).send_keys(parameters['Email'])
        if 'Current Address' in parameters:
            self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['current_address_input']).send_keys(
                parameters['Current Address'])
        if 'Permanent Address' in parameters:
            self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['permanent_address_input']).send_keys(
                parameters['Permanent Address'])
        self.driver.find_element(By.XPATH, TEXT_BOX_LOCATORS['submit_button']).click()
