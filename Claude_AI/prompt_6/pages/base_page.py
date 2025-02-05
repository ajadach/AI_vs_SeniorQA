from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, xpath):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

    def click_element(self, xpath):
        self.find_element(xpath).click()

    def input_text(self, xpath, text):
        element = self.find_element(xpath)
        element.clear()
        element.send_keys(text)

    def get_text(self, xpath):
        return self.find_element(xpath).text