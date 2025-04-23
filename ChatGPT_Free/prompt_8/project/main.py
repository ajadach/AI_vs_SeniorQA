from selenium import webdriver
from pages.text_box_page import TextBoxPage
from pages.web_tables_page import WebTablesPage

# Driver setup
driver = webdriver.Chrome()

# Interact with Text Box page
# text_box_page = TextBoxPage(driver)
# text_box_page.navigate_to_page()
#
# # Example of reading all parameters
# params = text_box_page.read_all_params()
# print("Text Box Params:", params)
#
# # Choosing parameters and submitting the form
# text_box_page.choose_parameters({
#     'Full Name': 'Artur',
#     'Email': 'artur@example.com',
#     'Current Address': 'Current Address Here',
#     'Permanent Address': 'Permanent Address Here'
# })

# Interact with Web Tables page
web_tables_page = WebTablesPage(driver)
web_tables_page.navigate_to_page()

# Reading all Web Table params
web_table_params = web_tables_page.read_all_params()
print("Web Tables Params:", web_table_params)

# Clean up
driver.quit()
