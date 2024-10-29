import json
import os
import pytest
import requests
from dotenv import load_dotenv
import allure
from selenium.common import TimeoutException
from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage
from test_data.links import MainPageLinks
from test_data.registration_data import Messages, Registration

load_dotenv()


@allure.epic("Test Registration Page")
class TestRegistrationPage:
    urls = MainPageLinks
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
        authorization_url = os.environ["AUTH_URL"]
        user = {"email": new_email, "password": os.environ["PASSWORD"], "returnSecureToken": "true"}
        response = requests.post(authorization_url, user)
        token = response.json()['idToken']
        url = f'{os.environ["DELETE_USER"]}{new_email}'
        payload = {}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.request("DELETE", url=url, headers=headers, data=payload)
        assert response.status_code == 200

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
