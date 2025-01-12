import imaplib
from random import choice
import allure
import os
from dotenv import load_dotenv
from selenium.common import TimeoutException
from locators.login_page_locators import LoginPageLocators
from locators.authotised_user_home_page_locators import AuthorizedUserHomePageLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from test_data.links import MainPageLinks

load_dotenv()


class ProfilePage(BasePage):

    @staticmethod
    def get_link_change_password_by_email():
        with allure.step('Get a link to change the password by email'):
            data_id = [b'']
            while data_id == [b'']:
                mail = imaplib.IMAP4_SSL('imap.mail.ru')
                mail.login(os.environ["CHANGE_PASSWORD_EMAIL"], os.environ["PASSWORD_EMAIL"])
                mail.select('INBOX')
                result, data_id = mail.search(None, 'UNSEEN')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            mail.logout()
            msg = str(data_id[0][1])
            first = msg.find(os.environ["PASSWORD_LINK"])
            link = msg[first:first + 186]
            return link

    @allure.step("Authorise user")
    def authorise_user(self):
        self.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["CHANGE_PASSWORD_EMAIL"])
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["CHANGE_PASSWORD"])
        self.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
        try:
            self.element_is_visible(LoginPageLocators.PASSWORD_RECOVERY)
        except TimeoutException:
            self.wait_changed_url(MainPageLinks.URL_PROFILE_PAGE)
        else:
            self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).clear()
            self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
            self.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()

    @allure.step("Open login page")
    def open_login_page(self):
        self.element_is_present_and_clickable(StartUnauthorizedPageLocators.SECTION_1_LINK_LOGIN).click()

    @allure.step("Go to the Profile page")
    def go_to_profile_page(self):
        self.element_is_present_and_clickable(AuthorizedUserHomePageLocators.PROFILE_USER).click()

    @allure.step("Click the button 'Change password'")
    def click_change_password_link(self):
        self.element_is_present_and_clickable(ProfilePageLocators.PASSWORD_RECOVERY).click()

    @allure.step("Clear field the email and enter data")
    def field_recovery_email(self):
        self.element_is_visible(ProfilePageLocators.EMAIL_INPUT).clear()
        self.element_is_visible(ProfilePageLocators.EMAIL_INPUT).send_keys(os.environ["CHANGE_PASSWORD_EMAIL"])

    @allure.step("Click the button 'Send recovery email'")
    def click_send_recovery_email_link(self):
        self.element_is_present_and_clickable(ProfilePageLocators.SEND_EMAIL).click()

    @allure.step("Enter the data in the email field")
    def enter_new_password_field(self):
        self.element_is_visible(ProfilePageLocators.NEW_PASSWORD).send_keys(choice([os.environ["CHANGE_PASSWORD"],
                                                                                    os.environ["PASSWORD"]]))

    @allure.step("Click the button 'SAVE'")
    def click_save_button(self):
        self.element_is_present_and_clickable(ProfilePageLocators.SAVE_BUTTON).click()

    @allure.step("Receive a successful message")
    def get_successful_message(self):
        return self.element_is_visible(ProfilePageLocators.SUCCESSFUL_MESSAGE)

    @allure.step("Check user's profile")
    def check_user_profile(self):
        return self.element_is_visible(ProfilePageLocators.PROFILE)

    @allure.step("Get error message")
    def get_error_message(self):
        return self.element_is_visible(ProfilePageLocators.WRONG_AUTH_DATA_MSG).text

    def authorisation_user(self, login, password):
        with allure.step('Fill the login'):
            self.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(login)
        with allure.step('Fill the password'):
            self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(password)
        with allure.step('Click the button submit'):
            self.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
        with allure.step('Wait changing url'):
            self.wait_changed_url(MainPageLinks.URL_PROFILE_PAGE)

    @allure.step("Loader checking")
    def loader_checking(self):
        self.timeout = 50
        return self.element_is_visible(ProfilePageLocators.TITLE)
