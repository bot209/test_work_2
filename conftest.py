import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    if browser_name == "chrome":
        print("\n Запускаю браузер 'chrome'")
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser_name == "firefox":
        print("\n Запускаю браузер 'firefox'")
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    yield browser
    print("\n Закрываю браузер")
    browser.quit()