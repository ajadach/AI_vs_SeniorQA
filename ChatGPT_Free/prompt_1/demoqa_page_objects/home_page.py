from demoqa_page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    ELEMENTS_CARD = (By.XPATH, "//h5[text()='Elements']")

    def navigate_to_elements(self):
        """Przejście do sekcji 'Elements'."""
        self.click_element(self.ELEMENTS_CARD)
