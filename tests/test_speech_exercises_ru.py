import allure

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.speech_exercises_page_api import SpeechExercisesAPI
from pages.speech_exercises_page_ru import SpeechExercisesPageRU


@allure.epic("Речевые упражнения.")
class TestCardsRU:
    @allure.suite('Слова.')
    @allure.title('Select random card from group "Слова" and compare UI vs BACKEND data.')
    def test_random_word_cards_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BUTTON_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_ru()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Слова Королёвой.')
    @allure.title('Select random card from group "Слова Королёвой" and compare UI vs BACKEND data.')
    def test_random_word_by_koroleva_cards_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BY_KOROLEVA_BUTTON)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_ru()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Похожие фразы')
    @allure.title('Select a random card from "Похожие фразы" group and compare UI vs BACKEND data.')
    def test_random_cards_in_similar_phrases_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_SIMILAR_PHRASES_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_ru()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Группа слов')
    @allure.title('Select a random card from "Группа слов" group and compare UI vs BACKEND data.')
    def test_random_cards_in_group_words_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_GROUP_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_for_group_words_ru()
        list_words_back = page.get_list_of_words_from_card_group_words(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Предложения.')
    @allure.title('Select a random card from "Предложения" group and compare UI vs BACKEND data.')
    def test_random_cards_in_sentences_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.SENTENCES_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_for_group_words_ru()
        list_words_back = page.get_list_of_words_from_card_group_words(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)

    @allure.suite('Слова с частотной группировкой')
    @allure.title('Select a random card from "Слова с частотной группировкой" group and compare UI vs BACKEND data.')
    def test_random_cards_in_words_with_frequency_grouping_ru(self, driver, specialist_user_authorized):
        page = SpeechExercisesPageRU(driver)
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_WITH_FREQUENCY_GROUPING_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        random_id = page.get_random_id_from_list_sub_group(
            card_id, seria_id)  # getting random ID from exercises group
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID
        page.wait_changed_url(driver.current_url)
        id_for_back = str(driver.current_url).split('/')[-1]
        list_words_ui = page.click_start_and_get_list_words_ru()
        list_words_back = page.get_list_of_words_from_card(f'{id_for_back}')
        assert sorted(list_words_ui) == sorted(list_words_back)
