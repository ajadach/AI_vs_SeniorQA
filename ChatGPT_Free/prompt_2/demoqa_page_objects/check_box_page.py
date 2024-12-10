from demoqa_page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckBoxPage(BasePage):
    TOGGLE_HOME = (By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-close")
    CHECK_DOCUMENTS = (By.XPATH, "//label[@for='tree-node-documents']//span[@class='rct-checkbox']")
    OUTPUT_SECTION = (By.ID, "result")

    def expand_home_directory(self):
        """Rozwija katalog główny."""
        self.click_element(self.TOGGLE_HOME)

    def select_documents(self):
        """Zaznacza opcję Documents."""
        self.click_element(self.CHECK_DOCUMENTS)

    def get_selected_items(self):
        """Zwraca wybrane elementy."""
        return self.find_element(self.OUTPUT_SECTION).text
