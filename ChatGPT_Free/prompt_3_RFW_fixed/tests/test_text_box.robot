*** Settings ***
Library    SeleniumLibrary
Library    demoqa_pages.elements_page.ElementsPage
Library    demoqa_pages.text_box_page.TextBoxPage

*** Variables ***
${BASE_URL}    https://demoqa.com/elements

*** Test Cases ***
Fill Text Box Form
    Open Browser    ${BASE_URL}    Chrome
    Maximize Browser Window
    Navigate To Text Box
    Fill Text Box Form    John Doe    johndoe@example.com    123 Main St    456 Another St
    ${output}=    Get Output Text
    Should Contain    ${output}    John Doe
    Should Contain    ${output}    johndoe@example.com
    Close Browser
