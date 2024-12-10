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

    def test_expand_all(self):
        """Test rozwijania całego drzewa folderów."""
        self.elements_page.navigate_to_check_box()

        self.check_box_page.expand_all()
        # Brak bezpośredniej asercji dla expand_all (opcja wizualna), więc można dodać dodatkowe kroki

    def test_select_specific_folder(self):
        """Test zaznaczenia konkretnego folderu."""
        self.elements_page.navigate_to_check_box()

        folder_name = "Downloads"
        self.check_box_page.expand_all()
        self.check_box_page.select_folder(folder_name)
        selected_items = self.check_box_page.get_selected_items()

        self.assertIn(folder_name.lower(), selected_items.lower())


if __name__ == "__main__":
    unittest.main()
    #python -m unittest tests/test_check_box.py