import allure

from pages.base_page import BasePage
from locators.locators import BasePageLocators
from test_data.links import MainPageLinks


class MainPage(BasePage):
    locators = BasePageLocators()

    def open_description_page(self):
        self.element_is_presence_and_clickable(self.locators.DESCRIPTION_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_DESCRIPTION_PAGE, \
            "The link leads to an incorrect page"

    def open_telegram_page(self):
        self.element_is_presence_and_clickable(self.locators.TELEGRAM_PAGE).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_TELEGRAM_PAGE, \
            "The link leads to an incorrect page"

    def open_donate_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.DONATE_PAGE).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_DONATE_PAGE, \
            "The link leads to an incorrect page"

    def open_contacts_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.CONTACTS).click()
        print(self.driver.current_url)
        assert self.driver.current_url == MainPageLinks.URL_CONTACTS, \
            "The link leads to an incorrect page"

    def open_specialists_page(self):
        with allure.step('Click button "MORE".'):
            self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        with allure.step('Click button "SPECIALISTS".'):
            self.element_is_presence_and_clickable(self.locators.SPECIALISTS_PAGE).click()
        with allure.step('Check page URL.'):
            self.check_expected_link(MainPageLinks.URL_SPECIALISTS_PAGE)
        self.get_current_url()

    def open_github(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.GITHUB).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_GITHUB, \
            "The link leads to an incorrect page"

    def open_contributors_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.CONTRIBUTORS_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_CONTRIBUTORS_PAGE, \
            "The link leads to an incorrect page"

    def open_used_resources_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.USED_RESOURCES_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_USED_RESOURCES_PAGE, \
            "The link leads to an incorrect page"
