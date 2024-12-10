from demoqa.pages.base_page import BasePage
from demoqa.locators.elements_locators import ElementsLocators
from selenium.webdriver.common.by import By


class ElementsPage(BasePage):
    CHECK_BOX_MENU = (By.XPATH, ElementsLocators.CHECK_BOX_MENU)

    def navigate_to_text_box(self):
        """Przejście do sekcji Text Box."""
        self.click_element(ElementsLocators.TEXT_BOX_MENU)

    def navigate_to_check_box(self):
        """Przejście do sekcji Check Box."""
        import pdb
        pdb.set_trace()
        self.click_element(self.CHECK_BOX_MENU)

    def navigate_to_web_tables(self):
        """Przejście do sekcji Web Tables."""
        self.click_element(ElementsLocators.WEB_TABLES_MENU)
