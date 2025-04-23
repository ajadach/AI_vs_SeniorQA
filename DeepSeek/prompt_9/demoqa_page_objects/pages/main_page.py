from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)  # Zwiększony timeout

    def navigate_to_elements_text_box(self):
        # Najpierw przewiń do elementu, jeśli jest potrzebne
        elements_card = self.wait.until(
            EC.presence_of_element_located((By.XPATH, MainPageLocators.ELEMENTS_CARD)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elements_card)
        elements_card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.ELEMENTS_CARD)))
        elements_card.click()

        text_box_item = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.TEXT_BOX_MENU_ITEM))
        )
        text_box_item.click()

    def navigate_to_elements_web_tables(self):
        # Najpierw przewiń do elementu
        elements_card = self.wait.until(
            EC.presence_of_element_located((By.XPATH, MainPageLocators.ELEMENTS_CARD)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elements_card)
        elements_card = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.ELEMENTS_CARD)))
        elements_card.click()

        web_tables_item = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, MainPageLocators.WEB_TABLES_MENU_ITEM))
        )
        web_tables_item.click()