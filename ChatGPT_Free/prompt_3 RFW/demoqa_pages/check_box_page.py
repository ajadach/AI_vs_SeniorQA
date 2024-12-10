from demoqa_pages.base_page import BasePage

class CheckBoxPage(BasePage):
    TOGGLE_HOME = "css:.rct-icon.rct-icon-expand-close"
    CHECK_DOCUMENTS = "xpath://label[@for='tree-node-documents']//span[@class='rct-checkbox']"
    OUTPUT_SECTION = "id:result"

    def expand_home(self):
        """Rozwija katalog główny."""
        self.click_element(self.TOGGLE_HOME)

    def select_documents(self):
        """Zaznacza opcję Documents."""
        self.click_element(self.CHECK_DOCUMENTS)

    def get_selected_items(self):
        """Zwraca wybrane elementy."""
        return self.get_element_text(self.OUTPUT_SECTION)
