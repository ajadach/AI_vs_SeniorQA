*** Settings ***
Library    SeleniumLibrary
Library    ..${/}demoqa_pages${/}ElementsPage.py
Library    ..${/}demoqa_pages${/}TextBoxPage.py

*** Variables ***
${BASE_URL}    https://demoqa.com/elements

*** Test Cases ***
Fill Text Box Form
    ElementsPage.Open Browser    ${BASE_URL}    Chrome
    ElementsPage.Maximize Browser Window
    ElementsPage.Navigate To Text Box
    TextBoxPage.Fill Text Box Form    John Doe    johndoe@example.com    123 Main St    456 Another St
    ${output}=    TextBoxPage.Get Output Text
    Should Contain    ${output}    John Doe
    Should Contain    ${output}    johndoe@example.com
    ElementsPage.Close Browser
