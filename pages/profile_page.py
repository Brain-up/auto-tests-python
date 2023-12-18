import imaplib
import time

import allure

from locators.locators import LoginPageLocators, BasePageLocators, AuthorizedUserHomePageLocators, ProfilePageLocators
from pages.base_page import BasePage


def get_link_change_password_by_email():
    with allure.step('Get a link to change the password by email'):
        mail = imaplib.IMAP4_SSL('imap.mail.ru')
        mail.login('test_brainup@mail.ru', 'cy6pvQyMFSWpRCpQHswD')
        mail.select('INBOX')
        result, data_id = mail.search(None, 'ALL')
        message_ids = data_id[0].split()
        result, data_id = mail.fetch(message_ids[-1], '(RFC822)')
        raw_email = str(data_id[0][1])
        mail.logout()
        # print(raw_email)
        first = raw_email.find('https://brainupspb.firebaseapp.com/__/auth/action?mode')
        link = raw_email[first:first + 186]
        return link


class ProfilePage(BasePage):

    @allure.step("The user has authorised")
    def user_has_authorised(self):
        self.element_is_visible(LoginPageLocators.INPUT_LOGIN).send_keys('test_brainup@mail.ru')
        self.element_is_visible(LoginPageLocators.INPUT_PASSWORD).send_keys('password')
        self.element_is_presence_and_clickable(LoginPageLocators.SIGN_IN_BUTTON).click()

    @allure.step("Open login page")
    def open_login_page(self):
        self.element_is_presence_and_clickable(BasePageLocators.LOGIN_BUTTON).click()

    @allure.step("Go to the Profile page")
    def go_to_profile_page(self):
        self.element_is_presence_and_clickable(AuthorizedUserHomePageLocators.PROFILE_USER).click()

    @allure.step("Click the button 'Change password'")
    def click_change_password_link(self):
        self.element_is_presence_and_clickable(ProfilePageLocators.PASSWORD_RECOVERY).click()

    @allure.step("Click the button 'Send recovery email'")
    def click_send_recovery_email_link(self):
        self.element_is_presence_and_clickable(ProfilePageLocators.SEND_EMAIL).click()
        time.sleep(5)

    @allure.step("Enter the data in the email field")
    def enter_new_password_field(self):
        self.element_is_visible(ProfilePageLocators.NEW_PASSWORD).send_keys('password')

    @allure.step("Click the button 'SAVE'")
    def click_save_button(self):
        self.element_is_presence_and_clickable(ProfilePageLocators.SAVE_BUTTON).click()

    @allure.step("Receive a successful message")
    def get_successful_message(self):
        return self.element_is_visible(ProfilePageLocators.SUCCESSFUL_MESSAGE)
