class TextBoxLocators:
    # Input fields
    FULL_NAME_INPUT = "//input[@id='userName']"
    EMAIL_INPUT = "//input[@id='userEmail']"
    CURRENT_ADDRESS_INPUT = "//textarea[@id='currentAddress']"
    PERMANENT_ADDRESS_INPUT = "//textarea[@id='permanentAddress']"
    SUBMIT_BUTTON = "//button[@id='submit']"

    # Output fields
    OUTPUT_NAME = "//p[@id='name']"
    OUTPUT_EMAIL = "//p[@id='email']"
    OUTPUT_CURRENT_ADDRESS = "//p[@id='currentAddress']"
    OUTPUT_PERMANENT_ADDRESS = "//p[@id='permanentAddress']"