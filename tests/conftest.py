import os
import allure
import pytest
from dotenv import load_dotenv
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from test_data.links import MainPageLinks

load_dotenv()


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_MAIN_PAGE}')
def main_page_open(driver):
    driver.get(MainPageLinks.URL_MAIN_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_DESCRIPTION_PAGE}')
def description_page_open(driver):
    driver.get(MainPageLinks.URL_DESCRIPTION_PAGE)


@pytest.fixture()
@allure.step('Auto test user authorized')
def auto_test_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    page.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
    return page


@pytest.fixture()
@allure.step('USER specialist authorized')
def specialist_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["SPECIALIST_LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    page.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
    return page


@pytest.fixture()
@allure.step('DEFAULT user authorized')
def default_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["DEFAULT_LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    current_page = page.get_current_url()
    page.wait_changed_url(current_page)
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    return page
