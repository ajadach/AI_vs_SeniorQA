"""Lokatory dla podstrony Text Box"""

class TextBoxLocators:
    FULL_NAME_INPUT = "//input[@id='userName']"
    EMAIL_INPUT = "//input[@id='userEmail']"
    CURRENT_ADDRESS_INPUT = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS_INPUT = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"

    # Lokatory dla wyświetlonych danych
    OUTPUT_BOX = "//div[@id='output']"
    OUTPUT_NAME = "//div[@id='output']//p[@id='name']"
    OUTPUT_EMAIL = "//div[@id='output']//p[@id='email']"
    OUTPUT_CURRENT_ADDRESS = "//div[@id='output']//p[@id='currentAddress']"
    OUTPUT_PERMANENT_ADDRESS = "//div[@id='output']//p[@id='permanentAddress']"