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

    @allure.suite('Слова.')
    @allure.title('Solutions to a random task in the "Слова" .')
    def test_solve_word_cards_ru(self, driver, default_user_authorized):
        page = SpeechExercisesPageRU(driver)
        page.click_button_exercises()
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BUTTON_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        payloads = page.get_random_id_from_list_sub_group_default(
            card_id, seria_id)  # getting random ID from exercises group
        random_id = page.get_random_id_from_payloads(payloads)
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID

        page.click_start_and_get_list_words_ru()
        page = SpeechExercisesPageRU(driver)
        message = page.get_correct_answer()
        assert message == 'Поздравляем! Упражнение выполнено!', 'Congratulation text is missing.'

    @allure.suite('Слова Королёвой.')
    @allure.title('Solutions to a random task in the "Слова Королёвой" .')
    def test_solve_koroleva_cards_ru(self, driver, default_user_authorized):
        page = SpeechExercisesPageRU(driver)
        page.click_button_exercises()
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BY_KOROLEVA_BUTTON)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        payloads = page.get_random_id_from_list_sub_group_default(
            card_id, seria_id)  # getting random ID from exercises group
        random_id = page.get_random_id_from_payloads(payloads)
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID

        page.click_start_and_get_list_words_ru()
        page = SpeechExercisesPageRU(driver)
        message = page.get_correct_answer()
        assert message == 'Поздравляем! Упражнение выполнено!', 'Congratulation text is missing.'

    @allure.suite('Слова.')
    @allure.title('Solutions to a random task in the "Слова" group and comparison of statics.')
    def test_solve_word_cards_with_statistic_ru(self, driver, default_user_authorized):
        page = SpeechExercisesPageRU(driver)
        table = page.get_statistic_data()
        start_result = list(table[1].values())[5]
        page.click_button_exercises()
        seria_id = page.select_group(SpeechExercisesPageLocators.WORDS_BUTTON_RU)
        card_id = page.click_random_card()
        page.wait_changed_url(driver.current_url)  # Wait until cards will be loaded

        page = SpeechExercisesAPI(driver)
        payloads = page.get_random_id_from_list_sub_group_default(
            card_id, seria_id)  # getting random ID from exercises group
        random_id = page.get_random_id_from_payloads(payloads)
        driver.get(driver.current_url + f'/exercise/{random_id}')  # Open the URL with the received card ID

        page.click_start_and_get_list_words_ru()
        page = SpeechExercisesPageRU(driver)
        message = page.get_correct_answer()
        assert message == 'Поздравляем! Упражнение выполнено!', 'Congratulation text is missing.'
        result = page.get_stats_data()
        middle_result = result[1].split(':')[-1]
        page.click_button_continue()
        table = page.get_statistic_data()
        finish_result = list(table[1].values())[5]
        assert int(start_result) + int(middle_result) == int(finish_result), 'Incorrect display of statistics data.'

    @allure.suite('Statistic.')
    @allure.title('Check statistic table.')
    def test_get_statistic_data(self, driver, default_user_authorized):
        page = SpeechExercisesPageRU(driver)
        table = page.get_statistic_data()
        print(table)
        assert table != {}
EMAIL="test4"
PASSWORD="testpassword"
BODY={"email":"test4","password":"testpassword"}