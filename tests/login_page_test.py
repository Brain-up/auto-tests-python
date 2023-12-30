import allure

from pages.autorized_user_home_page import AuthorizedUserHomePage
from pages.login_page import LoginPage
from pages.speech_exercises_page import SpeechExercisesPage
from pages.speech_exercises_words_page import SpeechExercisesWordsPage
from test_data.links import MainPageLinks


@allure.epic("Login Page.")
class TestLoginPage:

    @allure.title('Test for authorization customer.')
    def test_logining_user(self, driver, main_page_open):
        page = LoginPage(driver)
        login_page_url = page.login_user()
        assert login_page_url == MainPageLinks.URL_GROUPS_PAGE, "The link leads to an incorrect page"


@allure.epic("WORD.")
class TestCards:
    @allure.title('Select random card from word group and compare UI vs BACKEND data')
    def test_random_word_cards(self, driver, main_page_open):
        page = LoginPage(driver)
        page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        page.click_family_card()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesWordsPage(driver)
        random_id = page.get_random_id_from_list_all_family_cards()  # getting random ID from exercises group
        print(driver.current_url + f'/exercise/{random_id}')
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        list_words_ui = page.click_start_and_get_list_words()
        list_words_back = page.get_list_of_words_from_card(f'{random_id}')
        assert sorted(list_words_ui) == sorted(list_words_back)
