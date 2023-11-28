import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://brainup.site/'


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    else:
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
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

