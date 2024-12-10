import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTextBox(unittest.TestCase):
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

    def test_text_box_submission(self):
        """Test wypełnienia formularza Text Box."""

        # Przejdź do sekcji Text Box
        text_box_button = self.driver.find_element(By.ID, "item-0")
        text_box_button.click()

        # Wypełnij formularz
        self.driver.find_element(By.ID, "userName").send_keys("John Doe")
        self.driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")
        self.driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street")
        self.driver.find_element(By.ID, "permanentAddress").send_keys("456 Another Street")
        self.driver.find_element(By.ID, "submit").click()

        # Sprawdź wyniki
        output = self.driver.find_element(By.ID, "output").text
        self.assertIn("John Doe", output)
        self.assertIn("johndoe@example.com", output)
        self.assertIn("123 Main Street", output)
        self.assertIn("456 Another Street", output)


if __name__ == "__main__":
    unittest.main()
