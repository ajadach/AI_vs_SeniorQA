from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def navigate_to_text_box_page(self):
        self.driver.get("https://demoqa.com/elements")  # <--- Dodano
        self.click(By.XPATH, MainPageLocators.TEXT_BOX_LINK)

    def navigate_to_web_tables_page(self):
        self.driver.get("https://demoqa.com/elements")  # <--- Dodano
        self.click(By.XPATH, MainPageLocators.WEB_TABLES_LINK)