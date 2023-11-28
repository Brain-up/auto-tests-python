import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://brainup.site'


@pytest.fixture()
def driver():
    print('\nstart browser...')
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait


@pytest.fixture()
def main_page_open(driver):
    with allure.step(f'Open page: {URL}'):
        driver.get(URL)
        print('Open page:', URL)

