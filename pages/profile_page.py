import imaplib
import time
import allure
import os
from dotenv import load_dotenv
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.authotised_user_home_page_locators import AuthorizedUserHomePageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from test_data.links import MainPageLinks

load_dotenv()


class ProfilePage(BasePage):

    @staticmethod
    def get_link_change_password_by_email():
        with allure.step('Get a link to change the password by email'):
            mail = imaplib.IMAP4_SSL('imap.mail.ru')
            mail.login(os.environ["CHANGE_PASSWORD_EMAIL"], os.environ["PASSWORD_EMAIL"])
            mail.select('INBOX')
            result, data_id = mail.search(None, 'ALL')
            message_ids = data_id[0].split()
            result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
            raw_email = str(data_id[0][1])
            mail.logout()
            # print(raw_email)
            first = raw_email.find(os.environ["PASSWORD_LINK"])
            link = raw_email[first:first + 186]
            return link

    @allure.step("The user has authorised")
    def user_has_authorised(self):
        self.timeout = 20
        self.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["CHANGE_PASSWORD_EMAIL"])
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["CHANGE_PASSWORD"])
        self.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()
        self.wait_changed_url(MainPageLinks.URL_PROFILE_PAGE)

    @allure.step("Open login page")
    def open_login_page(self):
        self.element_is_present_and_clickable(MainPageLocators.LOGIN_BUTTON).click()

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
        time.sleep(10)

    @allure.step("Enter the data in the email field")
    def enter_new_password_field(self):
        self.element_is_visible(ProfilePageLocators.NEW_PASSWORD).send_keys(os.environ["PASSWORD"])

    @allure.step("Click the button 'SAVE'")
    def click_save_button(self):
        self.element_is_present_and_clickable(ProfilePageLocators.SAVE_BUTTON).click()

    @allure.step("Receive a successful message")
    def get_successful_message(self):
        return self.element_is_visible(ProfilePageLocators.SUCCESSFUL_MESSAGE)

    @allure.step("The user has authorised with new password")
    def user_has_authorised_with_new_password(self):
        self.timeout = 20
        self.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys(os.environ["CHANGE_PASSWORD_EMAIL"])
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys(os.environ["PASSWORD"])
        self.element_is_present_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()

    @allure.step("Enter old password in the email field")
    def enter_old_password_field(self):
        self.element_is_visible(ProfilePageLocators.NEW_PASSWORD).send_keys(os.environ["CHANGE_PASSWORD"])

    @allure.step("Check user's profile")
    def check_user_profile(self):
        return self.element_is_visible(ProfilePageLocators.PROFILE)

    @allure.step("Get error message")
    def get_error_message(self):
        return self.element_is_visible(ProfilePageLocators.WRONG_AUTH_DATA_MSG).text
