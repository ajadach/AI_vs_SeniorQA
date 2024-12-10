import unittest
from selenium import webdriver
from demoqa_page_objects.elements_page import ElementsPage
from demoqa_page_objects.text_box_page import TextBoxPage


class TextBoxTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_text_box_submission(self):
        elements_page = ElementsPage(self.driver)
        text_box_page = TextBoxPage(self.driver)

        elements_page.open_text_box()
        text_box_page.fill_form(
            name="John Doe",
            email="johndoe@example.com",
            current_address="123 Main St",
            permanent_address="456 Another St"
        )

        output = text_box_page.get_output_text()
        self.assertIn("John Doe", output)
        self.assertIn("johndoe@example.com", output)


if __name__ == "__main__":
    unittest.main()
    #python -m unittest tests/test_text_box.py