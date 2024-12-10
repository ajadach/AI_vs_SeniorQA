from BasePage import BasePage
from robot.api.deco import keyword

# AI_mistake: wrong file name - fixed
class ElementsPage(BasePage):
    TEXT_BOX_MENU = "id:item-0"
    CHECK_BOX_MENU = "id:item-1"

    #AI_mistake: Fixed added deco keyword
    @keyword("Navigate To Text Box")
    def navigate_to_text_box(self):
        """Przejście do sekcji Text Box."""
        self.element_click(self.TEXT_BOX_MENU)

    @keyword("Navigate To Check Box")
    def navigate_to_check_box(self):
        """Przejście do sekcji Check Box."""
        self.element_click(self.CHECK_BOX_MENU)
