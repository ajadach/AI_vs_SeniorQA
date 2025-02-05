class TextBoxLocators:
    FULL_NAME_INPUT = "//input[@id='userName']"
    EMAIL_INPUT = "//input[@id='userEmail']"
    CURRENT_ADDRESS_INPUT = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS_INPUT = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"
    OUTPUT_DIV = "//div[@id='output']"

class CheckBoxLocators:
    EXPAND_ALL = "//button[@title='Expand all']"
    HOME_CHECKBOX = "//span[contains(text(),'Home')]//ancestor::label"
    DESKTOP_CHECKBOX = "//span[contains(text(),'Desktop')]//ancestor::label"
    DOCUMENTS_CHECKBOX = "//span[contains(text(),'Documents')]//ancestor::label"
    DOWNLOADS_CHECKBOX = "//span[contains(text(),'Downloads')]//ancestor::label"
    RESULT_TEXT = "//div[@id='result']"

class WebTablesLocators:
    ADD_BUTTON = "//button[@id='addNewRecordButton']"
    SEARCH_BOX = "//input[@id='searchBox']"
    FIRST_NAME_INPUT = "//input[@id='firstName']"
    LAST_NAME_INPUT = "//input[@id='lastName']"
    EMAIL_INPUT = "//input[@id='userEmail']"
    AGE_INPUT = "//input[@id='age']"
    SALARY_INPUT = "//input[@id='salary']"
    DEPARTMENT_INPUT = "//input[@id='department']"
    SUBMIT_FORM = "//button[@id='submit']"
    DELETE_RECORD = "//span[@title='Delete']"
    EDIT_RECORD = "//span[@title='Edit']"