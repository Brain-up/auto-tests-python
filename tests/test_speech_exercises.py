import allure

from pages.autorized_user_home_page import AuthorizedUserHomePage
from pages.speech_exercises_page import SpeechExercisesPage
from pages.speech_exercises_page_api import SpeechExercisesAPI


@allure.epic("Speech exercises.")
class TestCards:
    @allure.suite('Words.')
    @allure.title('Select random card from word group and compare UI vs BACKEND data')
    def test_random_word_cards(self, driver, specialist_user_authorized):
        # page = LoginPage(driver)
        # page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
        print(page.get_current_url())
        random_id = page.get_random_id_from_list_sub_group_cards(card_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    def test_progress_bar_is_present(self, driver, specialist_user_authorized):
        # page = LoginPage(driver)
        # page.login_user()

        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises()

        page = SpeechExercisesPage(driver)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
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

    # @allure.suite('Similar phrases')
    # @allure.title('Select a random card from "Similar phrases" group and compare UI vs BACKEND data')
    # def test_random_cards_in_similar_phrases(self, driver, specialist_user_authorized):
    #     page = AuthorizedUserHomePage(driver)
    #     page.click_speech_exercises_01()
    #
    #     page = SpeechExercisesPage(driver)
    #     page.click_similar_phrases_card()
    #     card_id = page.click_random_card_in_similar_phrases()
    #     page.wait_changed_url(driver.current_url)
    #
    #     page = SpeechExercisesAPI(driver)
    #     random_id = page.get_random_id_from_list_sub_group_cards(card_id)  # getting random ID from exercises group
    #     driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
    #     page.wait_changed_url(driver.current_url)
    #     id_for_back = str(driver.current_url).split('/')[-1]
    #     list_words_ui = page.click_start_and_get_list_words()
    #     list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
    #     assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Similar phrases')
    @allure.title('Select a random card from "Similar phrases" group and compare UI vs BACKEND data')
    def test_random_cards_in_similar_phrases_v2(self, driver, specialist_user_authorized):
        page = AuthorizedUserHomePage(driver)
        page.click_speech_exercises_01()

        page = SpeechExercisesPage(driver)
        page.click_similar_phrases_card()
        card_id = page.click_random_sub_group_in_similar_phrases()

        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)

        random_id = page.get_random_id_from_list_sub_group_similar_cards(
            card_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)
