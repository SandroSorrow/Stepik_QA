from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help='Choose language.')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name.lower() == 'chrome':
        print('\nStart Google Chrome browser...\n')
        browser = webdriver.Chrome()
    elif browser_name.lower() == 'firefox':
        print('\nStar Mozilla Firefox browser...\n')
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('\nUnknown browser! Chrome or Firefox expected.\n')
    yield browser

    print(f'\nQuit {browser_name} browser.\n')
    # pause = input('Press any key: ')
    browser.quit()

