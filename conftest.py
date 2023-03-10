import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def browser():
    print('\nЗапускаю браузер')
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser
    print('\nЗакрываю браузер')