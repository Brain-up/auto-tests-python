import random

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
        current_url = self.get_current_url()
        with allure.step(f'Click button "{text_of_the_button.text}".'):
            self.element_is_present_and_clickable(selector_for_sub_group).click()
        try:
            self.wait_changed_url(current_url)  # Wait until cards will be loaded
            url = self.get_current_url()
            id_for_api_group = str(url).split('/')[-1]
            return id_for_api_group
        except Exception as ex:
            print(ex)
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
                self.element_is_present(self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER)
                answer_value = self.element_is_present(
                    self.locators.SpeechExercisesPageLocators.CORRECT_ANSWER).get_attribute(
                    'data-correct-answer')
                if answer_value != "undefined":
                    correct_card = self.element_is_present_and_clickable((By.XPATH, f'//*[text()="{answer_value}"]'))
                    self.action_move_to_element(correct_card)
                    correct_card.click()
                else:
                    message = self.element_is_present(self.locators.SpeechExercisesPageLocators.CONGRATULATION_MESSAGE)
                    print(message.text)
                    return message.text
        except Exception as ex:
            print(ex)
            message = self.element_is_present(self.locators.SpeechExercisesPageLocators.CONGRATULATION_MESSAGE)
            print(message.text)
            return message.text

    @allure.step('get_stats_data')
    def get_stats_data(self):
        result = [i.text for i in
                  self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_RESULT_SOLUTION)]
        print(result)
        return result

    @allure.step('click_button_continue')
    def click_button_continue(self):
        self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.CONTINUE_BUTTON_RU).click()
