import random
import allure
from locators import speech_exercises_page_locators as locators
from pages.base_page import BasePage
from test_data.links import MainPageLinks as Links


class SpeechExercisesPage(BasePage):
    locators = locators

    @allure.step('select_group')
    def select_group(self, selector_for_sub_group):
        with allure.step('Select Russian language. Click "EN" button.'):
            self.element_is_present_and_clickable(self.locators.AuthorizedUserHomePageLocators.EN_BUTTON).click()
        with allure.step('Click button "SPEECH EXERCISES".'):
            self.element_is_present_and_clickable(
                self.locators.AuthorizedUserHomePageLocators.SPEECH_EXERCISES_EN).click()
        text_of_the_button = self.element_is_present_and_clickable(selector_for_sub_group)
        print(f'Selected group is: {text_of_the_button.text}')
        with allure.step(f'Click button "{text_of_the_button.text}".'):
            self.element_is_present_and_clickable(selector_for_sub_group).click()

    @allure.step(f'Get seria ID from URL: {Links.URL_MAIN_PAGE}groups/4/series/9')
    def set_url_to_get_id_words_group(self):
        self.wait_url_to_be(f'{Links.URL_MAIN_PAGE}groups/4/series/9')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group

    @allure.step(f'Get seria ID from URL: {Links.URL_MAIN_PAGE}groups/4/series/10')
    def set_url_to_get_id_similar_phrase_group(self):
        self.wait_url_to_be(f'{Links.URL_MAIN_PAGE}groups/4/series/10')
        url = self.get_current_url()
        id_for_api_group = str(url).split('/')[-1]
        return id_for_api_group



    @allure.step('click_random_card_in_words')
    def click_random_card_in_words(self):
        self.element_is_present(self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)
        self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.WORDS_EN).click()
        list_cards_name = [
            i.text for i in self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)]
        print('list_cards_name', list_cards_name)
        id_card_from_list = random.randint(0, len(list_cards_name) - 1)
        print('Card ID in list is:', id_card_from_list + 1)
        random_card = self.elements_are_present(self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)[id_card_from_list]
        self.go_to_element(random_card)
        random_card.click()
        print('Selected sub group is:', random_card.text)
        return id_card_from_list

    @allure.step('check_button_interact')
    def check_button_interact(self):
        with allure.step('Check button "INTERACT" is present.'):
            button_interact = self.element_is_present_and_clickable(
                self.locators.SpeechExercisesPageLocators.BUTTON_INTERACT)
        with allure.step('Click button "INTERACT".'):
            button_interact.click()
            print('Clicked button INTERACT.')
            return button_interact

    @allure.step('check_button_solve')
    def check_button_solve(self):
        with allure.step('Check button "SOLVE" is present.'):
            button_solve = self.element_is_present_and_clickable(self.locators.SpeechExercisesPageLocators.BUTTON_SOLVE)
        with allure.step('Click button "SOLVE".'):
            button_solve.click()
            print('Clicked button SOLVE.')
            return button_solve

    @allure.step('check_progressbar')
    def check_progressbar(self):
        with allure.step('Check "progress-bar" is present after click button "SOLVE".'):
            progress_bar = self.elements_are_visible(self.locators.SpeechExercisesPageLocators.PROGRESS_BAR)
            return progress_bar

    # Methods for checking of exercises in the "Similar phrases" group
    @allure.step('click_random_sub_group_in_similar_phrases')
    def click_random_sub_group_in_similar_phrases(self):
        with allure.step('Wait until cards is present.'):
            self.element_is_present(self.locators.SpeechExercisesPageLocators.LIST_OF_LESSONS)
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
