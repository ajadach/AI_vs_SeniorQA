import unittest
from selenium import webdriver
from demoqa.pages.elements_page import ElementsPage
from demoqa.pages.check_box_page import CheckBoxPage


class TestCheckBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")
        cls.elements_page = ElementsPage(cls.driver)
        cls.check_box_page = CheckBoxPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_select_documents_check_box(self):
        """Test rozwinięcia drzewa i zaznaczenia opcji Documents."""
        self.elements_page.navigate_to_check_box()

        self.check_box_page.expand_home()
        self.check_box_page.select_documents()
        selected_items = self.check_box_page.get_selected_items()

        self.assertIn("documents", selected_items.lower())


if __name__ == "__main__":
    unittest.main()
    #python -m unittest tests/test_check_box.py