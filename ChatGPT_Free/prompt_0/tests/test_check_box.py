import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckBox(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Uruchamianie przeglądarki przed rozpoczęciem testów."""

        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://demoqa.com/elements")

    @classmethod
    def tearDownClass(cls):
        """Zamykanie przeglądarki po zakończeniu testów."""

        cls.driver.quit()

    def test_check_box_selection(self):
        """Test zaznaczenia opcji Documents w Check Box."""

        # Przejdź do sekcji Check Box
        check_box_button = self.driver.find_element(By.ID, "item-1")
        check_box_button.click()

        # Rozwiń katalog główny
        toggle_home = self.driver.find_element(By.CSS_SELECTOR, ".rct-icon.rct-icon-expand-close")
        toggle_home.click()

        # Zaznacz opcję "Documents"
        documents_checkbox = self.driver.find_element(By.XPATH, "//label[@for='tree-node-documents']//span[@class='rct-checkbox']")
        documents_checkbox.click()

        # Sprawdź, czy opcja "Documents" jest zaznaczona
        result_output = self.driver.find_element(By.ID, "result").text
        self.assertIn("documents", result_output.lower())


if __name__ == "__main__":
    unittest.main()
