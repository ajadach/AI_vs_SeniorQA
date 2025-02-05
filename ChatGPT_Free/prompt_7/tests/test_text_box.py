import pytest
from selenium import webdriver
from pages.text_box_page import TextBoxPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    yield driver
    driver.quit()


def test_text_box_crud(driver):
    page = TextBoxPage(driver)

    data = [
        ['Full Name', 'Artur'],
        ['Email', 'artur@example.com'],
        ['Current Address', 'Warsaw, Poland'],
        ['Permanent Address', 'Cracow, Poland']
    ]
    #
    # import pdb;
    # pdb.set_trace()

    # Create
    page.create(data)

    # Read
    result = page.read()

    assert result == {
        'Full Name': 'Artur',
        'Email': 'artur@example.com',
        'Current Address': 'Warsaw, Poland',
        'Permanent Address': 'Cracow, Poland'
    }

    # Update
    updated_data = [['Full Name', 'Kamil']]
    page.update(updated_data)
    result = page.read()
    assert result['Full Name'] == 'Kamil'

    # Delete
    page.delete()
    result = page.read()
    assert all(value == '' for value in result.values())
