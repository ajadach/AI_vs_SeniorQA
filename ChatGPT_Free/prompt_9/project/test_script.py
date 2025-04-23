from selenium import webdriver
from pages.main_page import MainPage
from pages.text_box_page import TextBoxPage
from pages.web_tables_page import WebTablesPage

# Inicjalizacja WebDriver
driver = webdriver.Chrome()

# Test
try:
    main_page = MainPage(driver)
    main_page.navigate_to_text_box_page()

    text_box_page = TextBoxPage(driver)
    text_box_page.navigate_to_page()

    params = {'Full Name': 'Artur', 'Email': 'artur@example.com'}
    text_box_page.choose_parameters(params)
    print(text_box_page.read_all_params())

    main_page.navigate_to_web_tables_page()

    web_tables_page = WebTablesPage(driver)
    web_tables_page.navigate_to_page()

    table_params = {
        'First Name': 'John', 'Last Name': 'Doe', 'Age': '30', 'Salary': '5000', 'Department': 'HR'
    }
    import pdb
    pdb.set_trace()
    web_tables_page.choose_parameters(table_params)
    print(web_tables_page.read_all_params())

finally:
    driver.quit()
