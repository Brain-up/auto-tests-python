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


@allure.epic("Speech exercises.")
class TestCards:
    @allure.suite('Words.')
    @allure.title('Check UI vs BACKEND data')
    @allure.description('Select random card from word group and compare UI vs BACKEND data')
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
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Words.')
    @allure.title('Checking the presence of buttons and progress-bar.')
    @allure.description('Checking the presence of buttons and progress-bar.')
    def test_progressbar_and_buttons_is_present(self, driver, main_page_open):
        page = LoginPage(driver)
        page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        page.click_family_card()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesWordsPage(driver)
        random_id = page.get_random_id_from_list_all_family_cards()  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        page.click_start_and_get_list_words()

        page = SpeechExercisesPage(driver)
        button_interact = page.check_button_interact()
        assert button_interact.text == 'INTERACT', 'Button "INTERACT" is not present.'
        button_solve = page.check_button_solve()
        assert button_solve.text == 'SOLVE', 'Button "SOLVE" is not present.'
        progress_bar = page.check_progressbar()
        assert bool(progress_bar) is True, 'Progress-bar is not present'
