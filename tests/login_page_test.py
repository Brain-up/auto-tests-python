import time

import allure
import pytest

from pages.autorized_user_home_page import AuthorizedUserHomePage
from pages.login_page import LoginPage
from pages.speech_exercises_page import SpeechExercisesPage
from test_data.links import MainPageLinks


@allure.epic("Login Page")
class TestLoginPage:

    def test_logining_user(self, driver, main_page_open):
        page = LoginPage(driver)
        login_page_url = page.login_user()
        assert login_page_url == MainPageLinks.URL_GROUPS_PAGE, "The link leads to an incorrect page"


@allure.epic("Exercises")
class TestTask:
    @pytest.mark.xfail(reason="Can't find element by locator ('xpath', '//a[@title='Речевые упражнения']')")
    def test_task(self, driver, main_page_open):
        page = LoginPage(driver)
        page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        page.click_family_card()

        time.sleep(5)

