from demoqa_pages.base_page import BasePage

class ElementsPage(BasePage):
    TEXT_BOX_MENU = "id:item-0"
    CHECK_BOX_MENU = "id:item-1"

    def navigate_to_text_box(self):
        """Przejście do sekcji Text Box."""
        self.click_element(self.TEXT_BOX_MENU)

    def navigate_to_check_box(self):
        """Przejście do sekcji Check Box."""
        self.click_element(self.CHECK_BOX_MENU)
