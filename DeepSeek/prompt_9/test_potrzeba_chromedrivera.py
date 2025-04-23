from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from demoqa_page_objects.pages.main_page import MainPage
from demoqa_page_objects.pages.text_box_page import TextBoxPage
from demoqa_page_objects.pages.web_tables_page import WebTablesPage
import time
import os

# Ścieżka do ChromeDriver - ZASTĄP TĄ WARTOŚĆ właściwą ścieżką
CHROME_DRIVER_PATH = r"C:\WebDriver\chromedriver.exe"

# Konfiguracja przeglądarki
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

# Sprawdzenie czy plik ChromeDriver istnieje
if not os.path.exists(CHROME_DRIVER_PATH):
    raise FileNotFoundError(
        f"ChromeDriver nie został znaleziony pod ścieżką: {CHROME_DRIVER_PATH}\n"
        "Pobierz odpowiednią wersję z https://chromedriver.chromium.org/downloads"
    )

try:
    # Inicjalizacja przeglądarki
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Otwarcie strony
    driver.get("https://demoqa.com")
    time.sleep(2)  # Krótka pauza na załadowanie strony

    # Main Page
    main_page = MainPage(driver)

    # Przejście do Text Box
    print("Przechodzę do Text Box...")
    main_page.navigate_to_elements_text_box()
    text_box_page = TextBoxPage(driver)

    # Wypełnienie formularza Text Box
    print("Wypełniam formularz Text Box...")
    params = {
        'Full Name': 'Artur Nowak',
        'Email': 'artur@example.com',
        'Current Address': 'ul. Testowa 123, Warszawa',
        'Permanent Address': 'ul. Stała 456, Kraków'
    }
    result = text_box_page.choose_parameters(params)
    print("Text Box Result:", result)

    # Powrót do strony głównej
    print("Wracam do strony głównej...")
    driver.get("https://demoqa.com")
    time.sleep(2)

    # Przejście do Web Tables
    print("Przechodzę do Web Tables...")
    main_page = MainPage(driver)  # Ponowna inicjalizacja po powrocie
    main_page.navigate_to_elements_web_tables()
    web_tables_page = WebTablesPage(driver)

    # Dodanie nowego rekordu do tabeli
    print("Dodaję nowy rekord do tabeli...")
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

except Exception as e:
    print(f"Wystąpił błąd: {str(e)}")
    raise

finally:
    # Zamknięcie przeglądarki
    if 'driver' in locals():
        print("Zamykam przeglądarkę...")
        driver.quit()