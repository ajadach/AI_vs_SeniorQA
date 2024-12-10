import unittest
from selenium import webdriver
from demoqa_page_objects.home_page import HomePage
from demoqa_page_objects.elements_page import ElementsPage


class DemoQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_text_box_submission(self):
        home_page = HomePage(self.driver)
        elements_page = ElementsPage(self.driver)

        home_page.open("https://demoqa.com/")
        home_page.navigate_to_elements()

        elements_page.open_text_box()
        elements_page.fill_text_box("John Doe", "johndoe@example.com")

        output_text = elements_page.get_output_text()
        self.assertIn("John Doe", output_text)
        self.assertIn("johndoe@example.com", output_text)


if __name__ == "__main__":
    unittest.main()
