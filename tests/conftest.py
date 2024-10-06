import os
import time

import allure
import pytest
from dotenv import load_dotenv

from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderUnauthorizedLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from pages.base_page import BasePage
from pages.profile_page import ProfilePage
from test_data.links import MainPageLinks

load_dotenv()


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_MAIN_PAGE}')
def main_page_open(driver):
    driver.get(MainPageLinks.URL_MAIN_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_CONTRIBUTORS_PAGE}')
def contributors_page_open(driver):
    driver.get(MainPageLinks.URL_CONTRIBUTORS_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_CONTACTS_PAGE}')
def contacts_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.LINK_CONTACTS).click()
    time.sleep(1)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_DESCRIPTION_PAGE}')
def description_page_open(driver):
    driver.get(MainPageLinks.URL_DESCRIPTION_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_LOGIN_PAGE}')
def login_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(StartUnauthorizedPageLocators.SECTION_1_LINK_LOGIN).click()
    time.sleep(1)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_SPECIALISTS_PAGE}')
def specialists_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.LINK_SPECIALISTS).click()
    time.sleep(1)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_USED_RESOURCES_PAGE}')
def used_resources_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(HeaderUnauthorizedLocators.LINK_USED_RESOURCES).click()
    time.sleep(1)


@pytest.fixture()
@allure.step('Auto test user authorized')
def auto_test_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    page.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
    page = ProfilePage(driver)
    page.loader_checking()


@pytest.fixture()
@allure.step('USER specialist authorized')
def specialist_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["SPECIALIST_LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    page.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
    page = ProfilePage(driver)
    page.loader_checking()


@pytest.fixture()
@allure.step('DEFAULT user authorized')
def default_user_authorized(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()
    page.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["DEFAULT_LOGIN"])
    page.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
    page.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
    page.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
    page = ProfilePage(driver)
    page.loader_checking()
