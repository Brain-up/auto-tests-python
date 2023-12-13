import allure

from locators.locators import BasePageLocators
from pages.base_page import BasePage
from test_data.links import MainPageLinks


class MainPage(BasePage):
    locators = BasePageLocators()

    @allure.step("Open description page")
    def open_description_page(self):
        self.element_is_presence_and_clickable(self.locators.DESCRIPTION_PAGE).click()
        self.check_expected_link(MainPageLinks.URL_DESCRIPTION_PAGE)
        return self.driver.current_url

    @allure.step("Open telegram page")
    def open_telegram_page(self):
        self.element_is_presence_and_clickable(self.locators.TELEGRAM_PAGE).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_TELEGRAM_PAGE)
        return self.driver.current_url

    @allure.step("Open donate page")
    def open_donate_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.DONATE_PAGE).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_DONATE_PAGE)
        return self.driver.current_url

    @allure.step("Open contacts page")
    def open_contacts_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.CONTACTS).click()
        self.check_expected_link(MainPageLinks.URL_CONTACTS)
        return self.driver.current_url

    @allure.step("Open specialists page")
    def open_specialists_page(self):
        with allure.step('Click button "MORE".'):
            self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        with allure.step('Click button "SPECIALISTS".'):
            self.element_is_presence_and_clickable(self.locators.SPECIALISTS_PAGE).click()
        with allure.step('Check page URL.'):
            self.check_expected_link(MainPageLinks.URL_SPECIALISTS_PAGE)
        return self.driver.current_url

    @allure.step("Open github page")
    def open_github(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.GITHUB).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_GITHUB)
        return self.driver.current_url

    @allure.step("Open contributors page")
    def open_contributors_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.CONTRIBUTORS_PAGE).click()
        self.check_expected_link(MainPageLinks.URL_CONTRIBUTORS_PAGE)
        return self.driver.current_url

    @allure.step("Open used resources page")
    def open_used_resources_page(self):
        self.element_is_presence_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_presence_and_clickable(self.locators.USED_RESOURCES_PAGE).click()
        self.check_expected_link(MainPageLinks.URL_USED_RESOURCES_PAGE)
        return self.driver.current_url
