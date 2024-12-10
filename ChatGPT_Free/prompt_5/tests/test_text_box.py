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
        """Test wypełnienia formularza Text Box i sprawdzenia wyników."""
        self.elements_page.navigate_to_text_box()

        name = "John Doe"
        email = "john.doe@example.com"
        current_address = "123 Current St"
        permanent_address = "456 Permanent Ave"

        self.text_box_page.fill_text_box_form(name, email, current_address, permanent_address)
        output_text = self.text_box_page.get_output_text()

        self.assertIn(name, output_text)
        self.assertIn(email, output_text)
        self.assertIn(current_address, output_text)
        self.assertIn(permanent_address, output_text)


if __name__ == "__main__":
    unittest.main()
