class CheckBoxLocators:
    # fixed xpath
    TOGGLE_HOME = '//*[@id="tree-node"]/ol/li/span/button'
    CHECK_DOCUMENTS = "//span[@class='rct-title' and text()='Documents']/preceding-sibling::span"
    OUTPUT_SECTION = "//div[@id='result']"
    EXPAND_ALL_BUTTON = "//button[@title='Expand all']"
    FOLDER_CHECKBOX = "//span[@class='rct-title' and text()='{}']/preceding-sibling::span"
