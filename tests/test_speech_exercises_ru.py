import allure

from pages.speech_exercises_page_api import SpeechExercisesAPI
from pages.speech_exercises_page_ru import SpeechExercisesPageRU


@allure.epic("Речевые упражнения.")
class TestCards:
    @allure.suite('Слова.')
    @allure.title('Select random card from word group and compare UI vs BACKEND data')
    def test_random_word_cards_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        page.click_speech_exercises()

        card_id = page.click_random_card_in_words()
        page.wait_changed_url(driver.current_url)

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group_words_cards_ru(
            card_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_ru()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)
