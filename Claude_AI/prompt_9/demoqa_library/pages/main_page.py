"""Klasa reprezentująca stronę główną DemoQA"""

from ..base_page import BasePage
from ..locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/"

    def navigate_to_page(self):
        self.visit(self.url)
        return self

    def navigate_to_elements(self):
        self.click(MainPageLocators.ELEMENTS_CARD)
        from .elements_page import ElementsPage
        return ElementsPage(self.driver)