import os
from dotenv import load_dotenv
import allure
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from test_data.links import MainPageLinks
from test_data.data import Messages, Data
load_dotenv()


@allure.epic("Test Registration Page")
class TestRegistrationPage:
    urls = MainPageLinks
    msg = Messages

    @allure.title('Check registration with an existing email')
    def test_registration_with_existing_email(self, driver, main_page_open):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(os.environ["CHANGE_PASSWORD_EMAIL"])
        page.fill_password(os.environ["CHANGE_PASSWORD"])
        page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message()
        assert text == self.msg.EXISTING_EMAIL, 'The user has registered with an existing email'

    @allure.title('Check registration with new email')
    def test_registration_with_new_email(self, main_page_open, driver):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(Data.EMAIL)
        page.fill_password(os.environ["CHANGE_PASSWORD"])
        page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        page.check_change_url()
        page = ProfilePage(driver)
        assert page.check_user_profile(), 'The user has not registered with a new email'

    @allure.title('Check registration with new email and empty confirm password')
    def test_registration_with_new_email_and_empty_confirm_password(self, main_page_open, driver):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(Data.EMAIL)
        page.fill_password(os.environ["CHANGE_PASSWORD"])
        page.fill_repeat_password('')
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message()
        assert text in self.msg.EMPTY_CONFIRM_PASSWORD, 'The user has registered without confirm password'

    @allure.title('Check registration with new email and empty password')
    def test_registration_with_new_email_and_empty_password(self, main_page_open, driver):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Data.FIRST_NAME)
        page.fill_birthday(Data.BIRTHDAY)
        page.choose_gender()
        page.fill_email(Data.EMAIL)
        page.fill_password('')
        page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message()
        assert text in self.msg.EMPTY_CONFIRM_PASSWORD, 'The user has registered without confirm password'
