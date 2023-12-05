from locators.locators import LoginPageLocators, BasePageLocators
from pages.base_page import BasePage
from test_data.data import Data
from test_data.links import MainPageLinks


class LoginPage(BasePage):
    locators = {'LoginPageLocators': LoginPageLocators(), 'BasePageLocators': BasePageLocators()}

    def login_user(self):
        self.element_is_presence_and_clickable(self.locators['BasePageLocators'].LOGIN_BUTTON).click()
        self.check_expected_link(MainPageLinks.URL_LOGIN_PAGE)
        self.element_is_presence(self.locators['LoginPageLocators'].INPUT_LOGIN).send_keys(Data.DEFAULT_USER_1['login'])
        self.element_is_presence(self.locators['LoginPageLocators'].INPUT_PASSWORD).send_keys(
            Data.DEFAULT_USER_1['password'])
        self.element_is_presence_and_clickable(self.locators['LoginPageLocators'].SIGN_IN_BUTTON).click()
        self.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
        return self.driver.current_url
