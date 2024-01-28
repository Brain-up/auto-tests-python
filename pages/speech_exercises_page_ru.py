import random

import allure

from locators import speech_exercises_page_locators as locators
from pages.base_page import BasePage


class SpeechExercisesPageRU(BasePage):
    locators = locators

    def select_group(self, selector_for_sub_group):
        with allure.step('Select Russian language. Click "RU" button.'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.RU_BUTTON).click()
        with allure.step('Click button "Речевые упражнения".'):
            self.element_is_present_and_clickable(
                self.locators.AuthorizedUserHomePageLocators.SPEECH_EXERCISES_RU).click()
        text_of_the_button = self.element_is_present_and_clickable(selector_for_sub_group)
        print(f'Selected group is: {text_of_the_button.text}')
        with allure.step(f'Click button "{text_of_the_button.text}".'):
            self.element_is_present_and_clickable(selector_for_sub_group).click()

    # Methods for Group Слова
    def click_random_card_in_words(self):
        with allure.step('Wait until cards is present.'):
            self.element_is_present(self.locators.SpeechExercisesPageLocators.FAMILY_CARD_RU)
        with allure.step('Click button "Words".'):
            self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.WORDS_BUTTON_RU).click()
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)[
            id_card_from_list]
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    # Methods for Group Слова Королёвой
    def click_random_card_in_words_by_koroleva(self):
        with allure.step('Wait until cards is present.'):
            self.element_is_present(self.locators.SpeechExercisesPageLocators.WORD_1_GROUP)
        with allure.step('Click button "Words 1 GROUP".'):
            self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.
                                                  WORDS_BY_KOROLEVA_BUTTON).click()
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)[
            id_card_from_list]
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    # Methods for Group Похожие фразы
    def click_random_card_in_similar_phrases_ru(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        print(list_cards_name)
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)[id_card_from_list - 1]
        print('random_card is:', random_card.text)
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    # Methods for Group Группа слов
    def click_random_card_in_group_words_ru(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        print(list_cards_name)
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)[id_card_from_list - 1]
        print('random_card is:', random_card.text)
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    # Methods for Group Предложения
    def click_random_card_in_sentences_ru(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        print(list_cards_name)
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)[id_card_from_list - 1]
        print('random_card is:', random_card.text)
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    # Methods for Group Слова с частотной группировкой
    def click_random_card_in_words_with_frequency_grouping_ru(self):
        # with allure.step('Wait until cards is present.'):
        #     self.element_is_present(self.locators.SpeechExercisesPageLocators.FAMILY_CARD_RU)
        with allure.step('Click button "Слова с частотной группировкой".'):
            self.element_is_present_and_clickable(
                self.locators.SpeechExercisesPageLocators.WORDS_WITH_FREQUENCY_GROUPING_RU).click()
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)]
        with allure.step(f'Getting list cards: {list_cards_name}'):
            pass
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        with allure.step(f'Select random id from list of cards. \nCard ID in list is:, {id_card_from_list + 1}'):
            print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)[id_card_from_list]
        with allure.step(f'Selected card is: {random_card.text}'):
            self.go_to_element(random_card)
            random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list
