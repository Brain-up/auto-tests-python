import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1920, 1080)
    else:
        chrome_options.add_argument("--window-size=1920,1080")
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
    yield driver
    print('\nquit browser...')
    driver.quit()
