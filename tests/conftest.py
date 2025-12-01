import os
import time

import allure
import pytest
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from locators.contacts_page_locators import ContactsPageLocators
from locators.contributors_page_locators import ContributorsPageLocators
from locators.exercises_ru_similar_phrases_page_locators import ExercisesRuSimilarPhrasesPageLocators as erspPL
from locators.exercises_ru_words_page_locators import ExercisesRuWordsPageLocators as erwPL
from locators.groups_page_locators import GroupsPageLocators
from locators.header_page_locators import HeaderUnauthorizedLocators as huLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from pages.base_page import BasePage
from pages.contributors_page import ContributorsPage
from pages.groups_page import GroupsPage
from pages.profile_page import ProfilePage
from test_data.links import MainPageLinks, ExercisesUrls

load_dotenv()


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_MAIN_PAGE}')
def main_page_open(driver):
    driver.get(MainPageLinks.URL_MAIN_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_CONTRIBUTORS_PAGE}')
def contributors_page_open(driver):
    driver.get(MainPageLinks.URL_CONTRIBUTORS_PAGE)
    page = ContributorsPage(driver)
    page.element_is_present(ContributorsPageLocators.PAGE_TITLE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_CONTACTS_PAGE}')
def contacts_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(huLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(huLocators.LINK_CONTACTS).click()
    page.element_is_present(ContactsPageLocators.PAGE_TITLE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_DESCRIPTION_PAGE}')
def description_page_open(driver):
    driver.get(MainPageLinks.URL_DESCRIPTION_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.STARTING_POINT} on the "ru" local')
def groups_ru_page_open1(driver, auto_test_user_authorized):
    page = GroupsPage(driver)
    ru_button = page.element_is_present_and_clickable(huLocators.RU_BUTTON)
    subtitles_before = [el.text for el in page.elements_are_located(GroupsPageLocators.PAGE_SUBTITLES)]
    ru_button.click()

    def subtitles_changed(driver):
        current_subtitles = [el.text for el in page.elements_are_located(GroupsPageLocators.PAGE_SUBTITLES)]
        return current_subtitles != subtitles_before and all(current_subtitles)

    Wait(driver, 20).until(subtitles_changed)
    page.elements_are_visible(GroupsPageLocators.PAGE_SUBTITLES)


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.STARTING_POINT} on the "ru" local')
def groups_ru_page_open(driver, auto_test_user_authorized):
    page = GroupsPage(driver)
    current_url_before = driver.current_url
    ru_button = page.element_is_present_and_clickable(huLocators.RU_BUTTON)
    ru_button.click()

    def url_locale_changed(driver):
        current_url = driver.current_url
        return current_url != current_url_before and "locale=ru-ru" in current_url

    Wait(driver, 20).until(url_locale_changed)
    page.elements_are_visible(GroupsPageLocators.PAGE_SUBTITLES)


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.STARTING_POINT}')
def groups_en_page_open(driver, auto_test_user_authorized):
    page = GroupsPage(driver)
    page.element_is_present_and_clickable(huLocators.EN_BUTTON).click()
    page.element_is_present(GroupsPageLocators.PAGE_TITLE)


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE} on the "ru" local')
def exercises_ru_similar_phrases_page_open(driver, groups_ru_page_open):
    driver.get(ExercisesUrls.URL_EXERCISES_RU_SIMILAR_PHRASES_PAGE)

    def page_fully_loaded(driver):
        ready_state = driver.execute_script("return document.readyState")
        if ready_state != "complete":
            return False

        try:
            content = driver.find_element(*erspPL.PAGE_LIST3)
            return content.is_displayed()
        except NoSuchElementException:
            return False

    Wait(driver, timeout=10).until(page_fully_loaded)
    Wait(driver, 10).until(EC.presence_of_all_elements_located(erspPL.PAGE_LIST3))


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.URL_EXERCISES_RU_WORDS_PAGE} on the "ru" local')
def exercises_ru_words_page_open(driver, groups_ru_page_open):
    driver.get(ExercisesUrls.URL_EXERCISES_RU_WORDS_PAGE)

    def page_fully_loaded(driver):
        ready_state = driver.execute_script("return document.readyState")
        if ready_state != "complete":
            return False

        try:
            content = driver.find_element(*erwPL.PAGE_LIST3)
            return content.is_displayed()
        except NoSuchElementException:
            return False

    Wait(driver, timeout=10).until(page_fully_loaded)
    Wait(driver, 10).until(EC.presence_of_all_elements_located(erwPL.PAGE_LIST3))


@pytest.fixture()
@allure.step(f'Open page: {ExercisesUrls.URL_EXERCISES_RU_WORDS_FAMILY_PAGE} on the "ru" local')
def exercises_ru_words_family_page_open(driver, groups_ru_page_open):
    driver.get(ExercisesUrls.URL_EXERCISES_RU_WORDS_FAMILY_PAGE)


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
    page.element_is_present_and_clickable(huLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(huLocators.LINK_SPECIALISTS).click()
    page.check_expected_link(MainPageLinks.URL_SPECIALISTS_PAGE)


@pytest.fixture()
@allure.step(f'Open page: {MainPageLinks.URL_USED_RESOURCES_PAGE}')
def used_resources_page_open(driver, main_page_open):
    page = BasePage(driver)
    page.element_is_present_and_clickable(huLocators.MORE_BUTTON).click()
    page.element_is_present_and_clickable(huLocators.LINK_USED_RESOURCES).click()
    page.check_expected_link(MainPageLinks.URL_USED_RESOURCES_PAGE)


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
