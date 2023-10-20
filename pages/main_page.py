from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import BasePageLocators
from test_data.links import MainPageLinks


class MainPage(BasePage):


    def open_description_page(self):
        self.driver.find_element(*BasePageLocators.DESCRIPTION_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_DESCRIPTION_PAGE, \
            "The link leads to an incorrect page"


    def open_telegram_page(self):
        self.driver.find_element(*BasePageLocators.TELEGRAM_PAGE).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_TELEGRAM_PAGE, \
            "The link leads to an incorrect page"

    def open_donate_page(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.DONATE_PAGE).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_DONATE_PAGE, \
            "The link leads to an incorrect page"

    def open_contacts_page(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.CONTACTS).click()
        assert self.driver.current_url == MainPageLinks.URL_CONTACTS, \
            "The link leads to an incorrect page"

    def open_specialists_page(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.SPECIALISTS_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_SPECIALISTS_PAGE, \
            "The link leads to an incorrect page"

    def open_github(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.GITHUB).click()
        self.switch_to_new_window()
        assert self.driver.current_url == MainPageLinks.URL_GITHUB, \
            "The link leads to an incorrect page"


    def open_contributors_page(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.CONTRIBUTORS_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_CONTRIBUTORS_PAGE, \
            "The link leads to an incorrect page"

    def open_used_resources_page(self):
        self.driver.find_element(*BasePageLocators.MORE_MENU).click()
        self.driver.find_element(*BasePageLocators.USED_RESOURCES_PAGE).click()
        assert self.driver.current_url == MainPageLinks.URL_USED_RESOURCES_PAGE, \
            "The link leads to an incorrect page"