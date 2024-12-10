# ChatGPT nie dał kodu mimo propozycji, było trzeba dodac prompt
# SECOND PROMPT: nie podałes kodu dla plików test_text_box.py i test_check_box.py
# ANSWER: Przepraszam za niedoprecyzowanie. Oto kod dla plików testowych test_text_box.py oraz

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
        self.elements_page.navigate_to_check_box()
        self.check_box_page.expand_home()
        self.check_box_page.select_documents()
        selected_items = self.check_box_page.get_selected_items()
        self.assertIn("documents", selected_items.lower())

if __name__ == "__main__":
    unittest.main()

    # python -m unittest .\demoqa\tests\test_check_box.py
    # python -m unittest test_check_box.py