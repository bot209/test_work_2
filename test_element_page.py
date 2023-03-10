import pytest
from pages.base_page import BasePage

url = 'https://demoqa.com/'


def test_element_page(browser):
    elem_page = BasePage(browser, url)
    elem_page.open()