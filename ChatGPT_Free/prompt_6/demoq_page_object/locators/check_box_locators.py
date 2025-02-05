class CheckBoxLocators:
    EXPAND_ALL = "//button[@aria-label='Expand all']"
    CHECKBOX_ITEM = "//span[contains(@class, 'rct-title') and text()='{}']"
    TOGGLE_ITEM = "//span[contains(@class, 'rct-text') and text()='{}']/preceding-sibling::button"
    CHECKED_ITEMS = "//span[contains(@class, 'rct-checkbox')]/input[@checked]"
