from robot.libraries.BuiltIn import BuiltIn

class BasePage:
    def __init__(self):
        self.selenium = BuiltIn().get_library_instance('SeleniumLibrary')

    def click_element(self, locator):
        self.selenium.click_element(locator)

    def input_text(self, locator, text):
        self.selenium.input_text(locator, text)

    def get_text(self, locator):
        return self.selenium.get_text(locator)