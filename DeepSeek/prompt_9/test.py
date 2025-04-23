from selenium import webdriver
from demoqa_page_objects.pages.main_page import MainPage
from demoqa_page_objects.pages.text_box_page import TextBoxPage
from demoqa_page_objects.pages.web_tables_page import WebTablesPage

# Inicjalizacja przeglądarki
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com")

# Main Page
main_page = MainPage(driver)

# Przejście do Text Box
main_page.navigate_to_elements_text_box()
text_box_page = TextBoxPage(driver)

# Wypełnienie formularza Text Box
params = {
    'Full Name': 'Artur Nowak',
    'Email': 'artur@example.com',
    'Current Address': 'ul. Testowa 123, Warszawa',
    'Permanent Address': 'ul. Stała 456, Kraków'
}
result = text_box_page.choose_parameters(params)
print("Text Box Result:", result)

# Przejście do Web Tables
main_page.navigate_to_elements_web_tables()
web_tables_page = WebTablesPage(driver)

# Dodanie nowego rekordu do tabeli
new_record = {
    'First Name': 'Jan',
    'Last Name': 'Kowalski',
    'Email': 'jan@example.com',
    'Age': '30',
    'Salary': '5000',
    'Department': 'IT'
}
result = web_tables_page.choose_parameters(new_record)
print("Web Tables Result:", result)

# Zamknięcie przeglądarki
driver.quit()