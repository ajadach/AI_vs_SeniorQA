"""Klasa reprezentująca podstronę Elements"""

from ..base_page import BasePage
from ..locators.elements_page_locators import ElementsPageLocators


class ElementsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://demoqa.com/elements"

    def navigate_to_page(self):
        self.visit(self.url)
        return self

    def navigate_to_text_box(self):
        self.click(ElementsPageLocators.TEXT_BOX_ITEM)
        from .text_box_page import TextBoxPage
        return TextBoxPage(self.driver)

    def navigate_to_web_tables(self):
        self.click(ElementsPageLocators.WEB_TABLES_ITEM)
        from .web_tables_page import WebTablesPage
        return WebTablesPage(self.driver)