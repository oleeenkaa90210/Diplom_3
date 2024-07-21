import pytest
from selenium import webdriver

from page_object.data import Urls


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser option")

    yield driver
    driver.quit()


@pytest.fixture
def open_stellar_burgers(driver):
    driver.get(Urls.SERVER_URL)

# pytest #запуск в Chrome
# pytest -s page_object/tests/ --browser firefox #запуск в Firefox
