import unittest
from selenium import webdriver
from demoqa_page_objects.elements_page import ElementsPage
from demoqa_page_objects.check_box_page import CheckBoxPage

class CheckBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_check_box_selection(self):
        elements_page = ElementsPage(self.driver)
        check_box_page = CheckBoxPage(self.driver)

        elements_page.open_check_box()
        check_box_page.expand_home_directory()
        check_box_page.select_documents()

        output = check_box_page.get_selected_items()
        self.assertIn("documents", output.lower())


if __name__ == "__main__":
    unittest.main()
    #python -m unittest tests/test_check_box.py
