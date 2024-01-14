import allure
import pytest

from test_data.links import MainPageLinks


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_MAIN_PAGE}')
def main_page_open(driver):
    driver.get(MainPageLinks.URL_MAIN_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_DESCRIPTION_PAGE}')
def description_page_open(driver):
    driver.get(MainPageLinks.URL_DESCRIPTION_PAGE)
