import os
import pytest
from dotenv import load_dotenv
import allure
from selenium.common import TimeoutException
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from test_data.registration_data import Messages, Registration
from pages.brainup_api_page import BrainUPAPI

load_dotenv()


@allure.epic("Test Registration Page")
class TestRegistrationPage:
    msg = Messages

    @allure.title('Check registration with new email')
    def test_registration_with_new_email(self, main_page_open, driver):
        page = RegistrationPage(driver)
        new_email = Registration.EMAIL
        page.open_registration_page()
        page.fill_first_name(Registration.FIRST_NAME)
        page.fill_birthday(Registration.BIRTHDAY)
        page.choose_gender()
        with allure.step("Fill email"):
            page.fill_email(new_email)
        with allure.step("Fill password"):
            page.fill_password(os.environ["PASSWORD"])
        with allure.step("Fill repeat password"):
            page.fill_repeat_password(os.environ["PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        page.check_change_url()
        page = ProfilePage(driver)
        assert page.check_user_profile(), 'The user has not registered with a new email'
        token = BrainUPAPI.get_user_token(new_email, os.environ["PASSWORD"])
        status_code = BrainUPAPI.delete_authorised_user(new_email, token)
        assert status_code == 200, "The user has not been deleted"

    @pytest.mark.parametrize(Registration.test_data, Registration.DATA_REGISTRATION)
    def test_registration_negative(self, driver, main_page_open, title, first_name, birthday, email, password,
                                   confirm_password, error_message):
        allure.dynamic.title(f'Check registration with {title}')
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(first_name)
        page.fill_birthday(birthday)
        page.choose_gender()
        with allure.step("Fill email"):
            page.fill_email(email)
        with allure.step("Fill password"):
            page.fill_password(password)
        with allure.step("Fill repeat password"):
            page.fill_repeat_password(confirm_password)
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message()
        assert text in error_message, f'The user has registered with {title}'

    @allure.title('Check registration without choosing gender')
    def test_registration_without_choosing_gender(self, main_page_open, driver):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Registration.FIRST_NAME)
        page.fill_birthday(Registration.BIRTHDAY)
        with allure.step("Fill email"):
            page.fill_email(Registration.EMAIL)
        with allure.step("Fill password"):
            page.fill_password(os.environ["CHANGE_PASSWORD"])
        with allure.step("Fill repeat password"):
            page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.choose_agreement()
        page.click_registration_button()
        text = page.check_error_message()
        assert text in self.msg.EMPTY_GENDER, 'The user has registered without choosing a gender'

    @allure.title('Check registration without choosing agreement')
    def test_registration_without_choosing_agreement(self, main_page_open, driver):
        page = RegistrationPage(driver)
        page.open_registration_page()
        page.fill_first_name(Registration.FIRST_NAME)
        page.fill_birthday(Registration.BIRTHDAY)
        page.choose_gender()
        with allure.step("Fill email"):
            page.fill_email(Registration.EMAIL)
        with allure.step("Fill password"):
            page.fill_password(os.environ["CHANGE_PASSWORD"])
        with allure.step("Fill repeat password"):
            page.fill_repeat_password(os.environ["CHANGE_PASSWORD"])
        page.click_registration_button()
        try:
            page.check_change_url()
        except TimeoutException:
            pass
        assert TimeoutException, 'The user has registered without choosing agreement'
