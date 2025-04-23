from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value):
        return self.find_element(by, value).text

    def wait_for_element(self, by, value, timeout=10):
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                return self.find_element(by, value)
            except:
                time.sleep(1)
        raise Exception(f"Element with locator {value} not found after {timeout} seconds")
