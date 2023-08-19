import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://brainup.site/'


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()


# @pytest.fixture(scope='function', autouse=True)
# def driver():
#     print('\nstart browser...')
#     options = Options()
#     # options.add_argument("--headless")
#     # options.add_argument("--no-sandbox")
#     # options.add_argument("--disable-dev-shm-usage")
#     # options.add_argument("--window-size=1382, 754")
#     driver = webdriver.Chrome(service=Service(), options=options)
#     # request.cls.driver = driver
#     driver.set_window_size(1382, 754)
#     yield driver
#     print('\nquit browser...')
#     driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait


@pytest.fixture(scope="function")
def main_page_open(driver):
    driver.get(URL)

