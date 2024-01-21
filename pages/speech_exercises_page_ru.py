import random

import allure

from locators import speech_exercises_page_locators as locators
from pages.base_page import BasePage


class SpeechExercisesPageRU(BasePage):
    locators = locators

    def click_speech_exercises(self):
        with allure.step('Select English language. Click "RU" button.'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.RU_BUTTON).click()
        with allure.step('Click button "Речевые упражнения".'):
            self.element_is_present_and_clickable(
                self.locators.AuthorizedUserHomePageLocators.SPEECH_EXERCISES_RU).click()
        with allure.step('Click button "Слова".'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.WORDS_BUTTON_RU).click()

    def click_family_card(self):
        with allure.step('Click button "Family card"'):
            self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.FAMILY_CARD_RU).click()

    def click_random_card_in_words(self):
        self.element_is_present(self.locators.SpeechExercisesPageLocators.FAMILY_CARD_RU)
        self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.WORDS_BUTTON_RU).click()
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)]
        id_card_from_list = random.randint(0, len(list_cards_name)-1)
        print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_CARD_FROM_WORDS_RU)[
            id_card_from_list]
        self.go_to_element(random_card)
        random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    def check_button_interact(self):
        with allure.step('Check button "INTERACT" is present.'):
            button_interact = self.element_is_present_and_clickable(
                self.locators.SpeechExercisesPageLocators.BUTTON_INTERACT)
        with allure.step('Click button "INTERACT".'):
            button_interact.click()
            print('Clicked button INTERACT.')
            return button_interact

    def check_button_solve(self):
        with allure.step('Check button "SOLVE" is present.'):
            button_solve = self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.BUTTON_SOLVE)
        with allure.step('Click button "SOLVE".'):
            button_solve.click()
            print('Clicked button SOLVE.')
            return button_solve

    def check_progressbar(self):
        with allure.step('Check "progress-bar" is present after click button "SOLVE".'):
            progress_bar = self.elements_are_visible(self.locators.SpeechExercisesPageLocators.PROGRESS_BAR)
            return progress_bar

    # Methods for checking of exercises in the "Similar phrases" group

    def click_similar_phrases_card(self):
        with allure.step('Click "Similar phrases" card'):
            self.element_is_present_and_clickable(
                self.locators.SpeechExercisesPageLocators.SIMILAR_PHRASES_GROUP).click()

    def click_random_sub_group_in_similar_phrases(self):
        list_cards_name = [i.text for i in self.elements_are_present(
            self.locators.SpeechExercisesPageLocators.CARDS_LIST_IN_SIMILAR_PHRASES)]
        print('Cards name on FRONT:', list_cards_name)
        print('Sub-group cards list len is: ', len(list_cards_name))
        id_card_from_list = random.randint(1, len(list_cards_name) - 1)
        print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.
                                                CARDS_LIST_IN_SIMILAR_PHRASES)[id_card_from_list]
        print('random_card is:', random_card.text)
        self.go_to_element(random_card)
        random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    def click_random_card_in_similar_phrases(self):
        list_cards_name = [i.text for i in
                           self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_CARDS_ID)]
        print(list_cards_name)
        id_card_from_list = random.randint(0, len(list_cards_name))
        print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_CARDS_ID)[
            id_card_from_list - 1]
        print('random_card is:', random_card.text)
        self.go_to_element(random_card)
        random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list
