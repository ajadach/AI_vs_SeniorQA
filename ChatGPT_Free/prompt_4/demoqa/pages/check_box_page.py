from demoqa.pages.base_page import BasePage
from demoqa.locators.check_box_locators import CheckBoxLocators

class CheckBoxPage(BasePage):
    def expand_home(self):
        """Rozwija katalog główny."""
        self.click_element(CheckBoxLocators.TOGGLE_HOME)

    def select_documents(self):
        """Zaznacza opcję Documents."""
        self.click_element(CheckBoxLocators.CHECK_DOCUMENTS)

    def get_selected_items(self):
        """Zwraca wybrane elementy."""
        return self.get_element_text(CheckBoxLocators.OUTPUT_SECTION)
