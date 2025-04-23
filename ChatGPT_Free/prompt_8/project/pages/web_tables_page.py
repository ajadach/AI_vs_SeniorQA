from selenium.webdriver.common.by import By
import lxml.html
from locators.web_tables_locators import WEB_TABLES_LOCATORS


class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get("https://demoqa.com/")
        self.driver.find_element(By.XPATH, "//*[text()='Elements']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Web Tables']").click()

    def read_all_params(self):
        inner_html = self.driver.find_element(By.XPATH, WEB_TABLES_LOCATORS['data']).get_attribute('innerHTML')
        root = lxml.html.fromstring(inner_html)
        divs = root.xpath(".//div")

        headers_inner_html = self.driver.find_element(By.XPATH, WEB_TABLES_LOCATORS['headers']).get_attribute(
            'innerHTML')
        headers_root = lxml.html.fromstring(headers_inner_html)
        headers_divs = headers_root.xpath(".//div")

        headers = [header.text.strip() for header in headers_divs]

        rows = []
        for div in divs:
            row = {}
            cells = div.xpath(".//div")
            for index, cell in enumerate(cells):
                row[headers[index]] = cell.text.strip() if cell.text else ''
            rows.append(row)
        return rows

    def choose_parameters(self, parameters):
        # Assuming there's an option to add or select parameters for Web Tables, we simulate row entry
        pass
