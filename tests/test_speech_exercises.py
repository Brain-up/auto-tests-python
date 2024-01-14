import allure

from pages.autorized_user_home_page import AuthorizedUserHomePage
from pages.login_page import LoginPage
from pages.speech_exercises_page import SpeechExercisesPage
from pages.speech_exercises_page_api import SpeechExercisesWordsPage


@allure.epic("Speech exercises.")
class TestCards:
    @allure.suite('Words.')
    @allure.title('Select random card from word group and compare UI vs BACKEND data')
    def test_random_word_cards(self, driver, specialist_user_authorized):
        page = LoginPage(driver)
        page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesWordsPage(driver)
        random_id = page.get_random_id_from_list_sub_group_cards(card_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    def test_progress_bar_is_present(self, driver, specialist_user_authorized):
        page = LoginPage(driver)
        page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesWordsPage(driver)
        random_id = page.get_random_id_from_list_sub_group_cards(card_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        page.click_start_and_get_list_words()

        page = SpeechExercisesPage(driver)
        button_interact = page.check_button_interact()
        assert button_interact.text == 'INTERACT'
        button_solve = page.check_button_solve()
        assert button_solve.text == 'SOLVE'
        progress_bar = page.check_progressbar()
        assert bool(progress_bar) is True
