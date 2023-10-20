import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait



URL = 'https://brainup.site/'


@pytest.fixture(scope="function")
def driver():
    print('\nstart browser...')
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1382,754")
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait


@pytest.fixture(scope="function")
def main_page_open(driver):
    driver.get(URL)

