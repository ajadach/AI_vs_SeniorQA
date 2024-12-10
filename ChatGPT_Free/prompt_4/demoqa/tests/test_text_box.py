# ChatGPT nie dał kodu mimo propozycji, było trzeba dodac prompt
# SECOND PROMPT: nie podałes kodu dla plików test_text_box.py i test_check_box.py
# ANSWER: Przepraszam za niedoprecyzowanie. Oto kod dla plików testowych test_text_box.py oraz

import unittest
from selenium import webdriver
from demoqa.pages.elements_page import ElementsPage
from demoqa.pages.text_box_page import TextBoxPage

class TestTextBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")
        cls.elements_page = ElementsPage(cls.driver)
        cls.text_box_page = TextBoxPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_fill_text_box_form(self):
        self.elements_page.navigate_to_text_box()
        self.text_box_page.fill_text_box_form(
            "John Doe", "johndoe@example.com", "123 Main St", "456 Another St"
        )
        output = self.text_box_page.get_output_text()
        self.assertIn("John Doe", output)
        self.assertIn("johndoe@example.com", output)
        self.assertIn("123 Main St", output)
        self.assertIn("456 Another St", output)

if __name__ == "__main__":
    unittest.main()
    # python -m unittest test_text_box.py
