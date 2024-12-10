import unittest
from selenium import webdriver
from demoqa.pages.elements_page import ElementsPage
from demoqa.pages.web_tables_page import WebTablesPage


class TestWebTables(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")
        cls.elements_page = ElementsPage(cls.driver)
        cls.web_tables_page = WebTablesPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_delete_row(self):
        self.elements_page.navigate_to_web_tables()
        initial_count = self.web_tables_page.get_rows_count()
        self.web_tables_page.delete_row("Cierra")
        final_count = self.web_tables_page.get_rows_count()
        self.assertEqual(initial_count - 1, final_count)

    def test_edit_row(self):
        self.elements_page.navigate_to_web_tables()
        self.web_tables_page.edit_row("Cierra", {
            "first_name": "UpdatedName",
            "last_name": "UpdatedLast",
            "email": "updated@example.com",
            "age": "30",
            "salary": "5000",
            "department": "HR"
        })
        # Możesz dodać dodatkowe sprawdzenia w zależności od wymagań.

if __name__ == "__main__":
    unittest.main()
