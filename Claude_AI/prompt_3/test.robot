DemoQA Elements Test Suite with SeleniumLibrary

*** Settings ***
Documentation    Test Suite for DemoQA Elements Page using Page Object Pattern
Library         SeleniumLibrary
Resource        resources/common.robot
Resource        resources/text_box_page.robot
Resource        resources/check_box_page.robot

*** Test Cases ***
Text Box Submission Test
    Open DemoQA Elements Page
    Navigate To Text Box
    Fill Text Box Form    Jan Kowalski    jan.kowalski@example.com    Adres 1    Adres 2
    Verify Text Box Output    Jan Kowalski

Check Box Selection Test
    Open DemoQA Elements Page
    Navigate To Check Box
    Expand Home Directory
    Select Home Checkbox
    Verify Checkbox Result Contains    desktop
    Verify Checkbox Result Contains    documents

*** Keywords ***
Open DemoQA Elements Page
    Open Browser    https://demoqa.com/elements    chrome
    Maximize Browser Window