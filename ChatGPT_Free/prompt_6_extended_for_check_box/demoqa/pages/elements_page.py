from demoqa.pages.base_page import BasePage
from demoqa.locators.elements_locators import ElementsLocators

class ElementsPage(BasePage):
    def navigate_to_text_box(self):
        """Przejście do sekcji Text Box."""
        self.click_element(ElementsLocators.TEXT_BOX_MENU)

    def navigate_to_check_box(self):
        """Przejście do sekcji Check Box."""
        self.click_element(ElementsLocators.CHECK_BOX_MENU)

    def navigate_to_web_tables(self):
        """Przejście do sekcji Web Tables."""
        self.click_element(ElementsLocators.WEB_TABLES_MENU)
