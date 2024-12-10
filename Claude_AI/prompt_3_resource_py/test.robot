*** Settings ***
Library     SeleniumLibrary
Library     pages/text_box_page.py
Library     pages/check_box_page.py

Suite Setup     Open Browser    https://demoqa.com/elements    chrome
Suite Teardown  Close Browser

*** Test Cases ***
Text Box Submission Test
    ${text_box_page}=    TextBoxPage
    ${text_box_page.navigate_to}
    ${text_box_page.fill_form}    Jan Kowalski    jan.kowalski@example.com    Adres 1    Adres 2
    ${output_name}=    ${text_box_page.get_output_name}
    Should Contain    ${output_name}    Jan Kowalski

Check Box Selection Test
    ${check_box_page}=    CheckBoxPage
    ${check_box_page.navigate_to}
    ${check_box_page.expand_home_directory}
    ${check_box_page.select_home_checkbox}
    ${result_text}=    ${check_box_page.get_result_text}
    Should Contain    ${result_text}    desktop
    Should Contain    ${result_text}    documents