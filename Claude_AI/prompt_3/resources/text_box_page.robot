*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${TEXT_BOX_MENU}            xpath=//span[contains(text(), 'Text Box')]
${FULL_NAME_INPUT}          id=userName
${EMAIL_INPUT}              id=userEmail
${CURRENT_ADDRESS_INPUT}    id=currentAddress
${PERMANENT_ADDRESS_INPUT}  id=permanentAddress
${SUBMIT_BUTTON}            id=submit
${OUTPUT_NAME}              xpath=//p[@id='name']

*** Keywords ***
Navigate To Text Box
    Click Element    ${TEXT_BOX_MENU}

Fill Text Box Form
    [Arguments]    ${full_name}    ${email}    ${current_address}    ${permanent_address}
    Input Text    ${FULL_NAME_INPUT}            ${full_name}
    Input Text    ${EMAIL_INPUT}                ${email}
    Input Text    ${CURRENT_ADDRESS_INPUT}      ${current_address}
    Input Text    ${PERMANENT_ADDRESS_INPUT}    ${permanent_address}
    Click Button    ${SUBMIT_BUTTON}

Verify Text Box Output
    [Arguments]    ${expected_name}
    Element Should Contain    ${OUTPUT_NAME}    ${expected_name}