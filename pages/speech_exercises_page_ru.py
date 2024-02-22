import random
import time

import allure
from selenium.webdriver.common.by import By

from locators import speech_exercises_page_locators as locators
from pages.base_page import BasePage


class SpeechExercisesPageRU(BasePage):
    locators = locators

    @allure.step('select_group')
    def select_group(self, selector_for_sub_group):
        """
        Select random group and return id number from getting url
        :param selector_for_sub_group: Any
        :return str(id)
        """
        with allure.step('Select Russian language. Click "RU" button.'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.RU_BUTTON).click()
        with allure.step('Click button "Речевые упражнения".'):
            self.element_is_present_and_clickable(
                self.locators.AuthorizedUserHomePageLocators.SPEECH_EXERCISES_RU).click()
        text_of_the_button = self.element_is_present_and_clickable(selector_for_sub_group)
        print(f'Selected group is: {text_of_the_button.text}')
        with allure.step(f'Click button "{text_of_the_button.text}".'):
            self.element_is_present_and_clickable(selector_for_sub_group).click()

    def set_url_to_get_id_words_ru_group(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/1')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    def set_url_to_get_id_words_koroleva_ru_group(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/17')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    def set_url_to_get_id_similar_phrase_ru_group(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/2')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    def set_url_to_get_id_words_group_ru_group(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/3')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    def set_url_to_get_id_sentences_ru_group(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/4')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    def set_url_to_get_id_words_with_frequency_grouping(self):
        self.wait_url_to_be('https://brainup.site/groups/2/series/6')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    # Methods for Group Слова
    @allure.step('click_random_card')
    def click_random_card(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)[
            id_card_from_list]
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    @allure.step('click_random_card_for_solve')
    def click_random_card_for_solve(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.AVAILABLE_EXERCISES)[
            id_card_from_list]
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    @allure.step('get_correct_answer')
    def get_correct_answer(self):
        try:
            while True:
                time.sleep(1)
                self.element_is_present(self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER)
                answer_value = self.element_is_present(
                    self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER).get_attribute(
                    'data-correct-answer')
                print('Answer_value: ', answer_value)

                if answer_value != "undefined" and ',' not in answer_value:
                    try:
                        correct_card = self.element_is_present_and_clickable(
                            (By.XPATH, f'//*[text()="{answer_value}"]'))
                        self.action_move_to_element(correct_card)
                        correct_card.click()
                    except Exception as ex:
                        print(ex)
                        correct_card = self.element_is_present_and_clickable(
                            (By.XPATH, f'//*[text()="{answer_value}"]'))
                        self.action_move_to_element(correct_card)
                        correct_card.click()
                elif ',' in answer_value:
                    time.sleep(1)
                    self.element_is_present(self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER)
                    answer_value = self.element_is_present(
                        self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER).get_attribute(
                        'data-correct-answer')
                    list_answers = answer_value.split(',')
                    for answer in list_answers:
                        print('answer', answer_value)
                        try:
                            correct_card = self.element_is_present_and_clickable(
                                (By.XPATH, f'//*[text()="{answer}"]'))
                            self.action_move_to_element(correct_card)
                            correct_card.click()
                        except Exception as ex:
                            print(ex)
                            correct_card = self.element_is_present_and_clickable(
                                (By.XPATH, f'//*[text()="{answer}"]'))
                            self.action_move_to_element(correct_card)
                            correct_card.click()
                else:
                    message = self.element_is_present(self.locators.SpeechExercisesPageLocators.CONGRATULATION_MESSAGE)
                    print(message.text)
                    return message.text
        except Exception as ex:
            print(ex)
            message = self.element_is_present(self.locators.SpeechExercisesPageLocators.CONGRATULATION_MESSAGE)
            return message.text

    @allure.step('get_result_data')
    def get_stats_data(self):
        result = [i.text for i in
                  self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_RESULT_SOLUTION)]
        with allure.step(f'Result is: {result}'):
            pass
        return result

    @allure.step('Click button "Продолжить".')
    def click_button_continue(self):
        self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.CONTINUE_BUTTON_RU).click()

    @allure.step('get_statistic_data')
    def get_statistic_data(self):
        with allure.step('Click button "Статистика"".'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.STATISTIC_BUTTON).click()
        with allure.step('Check statistic table is present and scroll to table'):
            table = self.element_is_present(self.locators.AuthorizedUserHomePageLocators.STATISTIC_TABLE)
            self.go_to_element(table)
        with allure.step('Get data from the table.'):
            lens = len(self.elements_are_present((By.XPATH, "//tbody/tr")))
            titles = self.elements_are_present(self.locators.AuthorizedUserHomePageLocators.STATISTIC_DATA_TITLES)
            title = [i.text for i in titles]
            table = {}
            for i in range(1, lens + 1):
                table.setdefault(i, {})
                for j in range(len(title)):
                    try:
                        table[i].setdefault(title[j],
                                            self.element_is_present((By.XPATH, f"//tbody/tr[{i}]/td[{j + 1}]")).text)
                    except Exception as ex:
                        print(ex)
                        table[i].setdefault(title[j],
                                            self.element_is_present((By.XPATH, f"//tbody/tr[{i}]/td[{j + 1}]")).text)
        with allure.step(f'Table data: {table}'):
            pass
        return table

    @allure.step('Click button "Упражнения".')
    def click_button_exercises(self):
        with allure.step('Click button "RU".'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.RU_BUTTON).click()
        button = self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.BUTTON_EXERCISES_RU)
        self.go_to_element(button)
        self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.BUTTON_EXERCISES_RU).click()

    @allure.step('click_button RU')
    def click_button_ru(self):
        with allure.step('Click button "RU".'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.RU_BUTTON).click()
