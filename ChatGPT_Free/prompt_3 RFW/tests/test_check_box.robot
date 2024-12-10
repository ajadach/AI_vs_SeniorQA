*** Settings ***
Library    SeleniumLibrary
Library    demoqa_pages.elements_page.ElementsPage
Library    demoqa_pages.check_box_page.CheckBoxPage

*** Variables ***
${BASE_URL}    https://demoqa.com/elements

*** Test Cases ***
Select Check Box
    Open Browser    ${BASE_URL}    Chrome
    Maximize Browser Window
    Navigate To Check Box
    Expand Home
    Select Documents
    ${output}=    Get Selected Items
    Should Contain    ${output}    documents
    Close Browser
