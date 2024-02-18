import allure
import pytest

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.speech_exercises_page_api import SpeechExercisesAPI
from pages.speech_exercises_page_en import SpeechExercisesPage


@allure.epic("Speech exercises.")
class TestCardsEN:
    @pytest.mark.xfail
    @allure.suite('Words.')
    @allure.title('Select random card from "Word" group and compare UI vs BACKEND data')
    def test_random_word_cards_en(self, driver, specialist_user_authorized):
        page = SpeechExercisesPage(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.SIMILAR_PHRASES_EN)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_en()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @pytest.mark.xfail
    @allure.suite('Check progres-bar and buttons.')
    @allure.title('test_progress_bar_is_present_en')
    def test_progress_bar_is_present_en(self, driver, specialist_user_authorized):
        page = SpeechExercisesPage(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BUTTON_EN)
        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        page.click_start_and_get_list_words_en()

        page = SpeechExercisesPage(driver)
        button_interact = page.check_button_interact()
        assert button_interact.text == 'INTERACT'
        button_solve = page.check_button_solve()
        assert button_solve.text == 'SOLVE'
        progress_bar = page.check_progressbar()
        assert bool(progress_bar) is True

    @pytest.mark.xfail
    @allure.suite('Similar phrases')
    @allure.title('Select a random card from "Similar phrases" group and compare UI vs BACKEND data')
    def test_random_cards_in_similar_phrases_en(self, driver, specialist_user_authorized):
        page = SpeechExercisesPage(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.SIMILAR_PHRASES_EN)
        card_id = page.click_random_sub_group_in_similar_phrases()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_en()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)
