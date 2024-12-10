*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CHECK_BOX_MENU}       xpath=//span[contains(text(), 'Check Box')]
${HOME_EXPAND_BTN}      xpath=//button[@title='Toggle']
${HOME_CHECKBOX}        xpath=//label[@for='tree-node-home']//span[@class='rct-checkbox']
${RESULT_TEXT}          id=result

*** Keywords ***
Navigate To Check Box
    Click Element    ${CHECK_BOX_MENU}

Expand Home Directory
    Click Element    ${HOME_EXPAND_BTN}

Select Home Checkbox
    Click Element    ${HOME_CHECKBOX}

Verify Checkbox Result Contains
    [Arguments]    ${expected_text}
    Element Should Contain    ${RESULT_TEXT}    ${expected_text}