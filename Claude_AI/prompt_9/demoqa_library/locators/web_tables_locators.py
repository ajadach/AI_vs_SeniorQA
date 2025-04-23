"""Lokatory dla podstrony Web Tables"""


class WebTablesLocators:
    ADD_BUTTON = "//button[@id='addNewRecordButton']"
    SEARCH_BOX = "//input[@id='searchBox']"

    # Tabela i dane
    TABLE = "//div[@class='rt-table']"
    TABLE_ROWS = "//div[@class='rt-tr-group']"
    ROW_CELLS = "//div[contains(@class, 'rt-td')]"

    # Edycja/Usuwanie rekordu
    EDIT_RECORD_BUTTON = "//span[@title='Edit']"
    DELETE_RECORD_BUTTON = "//span[@title='Delete']"

    # Formularz
    REGISTRATION_FORM = "//div[@class='modal-content']"
    FIRST_NAME_INPUT = "//input[@id='firstName']"
    LAST_NAME_INPUT = "//input[@id='lastName']"
    EMAIL_INPUT = "//input[@id='userEmail']"
    AGE_INPUT = "//input[@id='age']"
    SALARY_INPUT = "//input[@id='salary']"
    DEPARTMENT_INPUT = "//input[@id='department']"
    SUBMIT_FORM_BUTTON = "//button[@id='submit']"
    CLOSE_FORM_BUTTON = "//button[text()='Close']"
