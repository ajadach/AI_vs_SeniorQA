from demoqa_page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class ElementsPage(BasePage):
    TEXT_BOX_MENU = (By.ID, "item-0")
    CHECK_BOX_MENU = (By.ID, "item-1")

    def open_text_box(self):
        """Przejście do sekcji Text Box."""
        self.click_element(self.TEXT_BOX_MENU)

    def open_check_box(self):
        """Przejście do sekcji Check Box."""
        self.click_element(self.CHECK_BOX_MENU)
