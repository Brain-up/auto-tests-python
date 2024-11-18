import json
import os
import random
import allure
import requests
from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.base_page import BasePage
from dotenv import load_dotenv
from test_data.links import MainPageLinks as Links

load_dotenv()

authorization_url = os.environ["AUTH_URL"]
data_specialist_user = {"email": os.environ["SPECIALIST_LOGIN"], "password": os.environ["PASSWORD"],
                        "returnSecureToken": "true"}
result_post_specialist = requests.post(authorization_url, data_specialist_user)
id_token = json.loads(result_post_specialist.text)['idToken']

data_default_user = {"email": os.environ["DEFAULT_LOGIN"], "password": os.environ["PASSWORD"],
                     "returnSecureToken": "true"}
result_post_default = requests.post(authorization_url, data_default_user).json()
id_token_default = result_post_default['idToken']


class SpeechExercisesAPI(BasePage):
    locators = SpeechExercisesPageLocators()

    @staticmethod
    @allure.step('get_random_id_from_list_sub_group')
    def get_random_id_from_list_sub_group(card_id, seria_id):
        print('Card_id is:', card_id)
        print('Seria_id is:', seria_id)
        list_cards_id = requests.get(f'{Links.URL_MAIN_PAGE}api/subgroups?seriesId={seria_id}',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token)})
        with allure.step(f'Status code is: {list_cards_id.status_code}'):
            pass
        with allure.step(
                f'Send GET request with params: '
                f'{Links.URL_MAIN_PAGE}api/subgroups?seriesId={seria_id}'
                f'headers="Content-Type": "application/json","Authorization": "Bearer": "{{id_token}}"'):
            pass
        with allure.step(f'Getting list of cards id: {list_cards_id.json()}'):
            pass
        result_get = json.loads(list_cards_id.text)
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        with allure.step(f'Select random id from list: {id_number}'):
            pass
        print('Nuber exercise on backend is: ', id_number)
        return id_number

    # General methods
    @staticmethod
    @allure.step('get_list_of_words_from_card')
    def get_list_of_words_from_card(card_id):
        result_get = requests.get(f'{Links.URL_MAIN_PAGE}api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        with allure.step(f'Status code is: {result_get.status_code}'):
            pass
        amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
        words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    @staticmethod
    @allure.step('get_list_of_words_from_card_group_words')
    def get_list_of_words_from_card_group_words(card_id):
        result_get = requests.get(f'{Links.URL_MAIN_PAGE}api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        with allure.step(f'Status code is: {result_get.status_code}'):
            pass
        dict_list = json.loads(result_get.text)['data']["answerOptions"]
        words = []
        for k, v in dict_list.items():
            for i in range(len(dict_list[k])):
                words.append(dict_list[k][i]['word'])
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    @allure.step('click_start_and_get_list_words_en')
    def click_start_and_get_list_words_en(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_EN).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_IN_CARD)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        return words

    @allure.step('click_start_and_get_list_words_ru')
    def click_start_and_get_list_words_ru(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_RU).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_IN_CARD)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        with allure.step('Click button "Повторить".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_REPEAT_RU).click()
        with allure.step('Click button "Решать".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_SOLVE_RU).click()
        return words

    @allure.step('click_start_and_get_list_words_for_group_words_ru')
    def click_start_and_get_list_words_for_group_words_ru(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START_RU).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_FOR_GROUP_WORDS)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        return words

    @staticmethod
    @allure.step('get_random_id_from_list_sub_group_default')
    def get_random_id_from_list_sub_group_default(card_id, seria_id):
        print('Card_id is:', card_id)
        print('Seria_id is:', seria_id)
        list_cards_id = requests.get(f'{Links.URL_MAIN_PAGE}api/subgroups?seriesId={seria_id}',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token_default)})
        with allure.step(f'Status code is: {list_cards_id.status_code}'):
            pass
        with allure.step(
                f'Send GET request with params: '
                f'{Links.URL_MAIN_PAGE}api/subgroups?seriesId={seria_id}'
                f'headers="Content-Type": "application/json","Authorization": "Bearer": "{{id_token_default}}"'):
            pass
        with allure.step(f'Getting list of cards id: {list_cards_id.json()}'):
            pass
        result_get = json.loads(list_cards_id.text)
        payloads = {}
        payloads.setdefault('ids', result_get['data'][card_id]['exercises'])
        print('payloads', payloads)
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        with allure.step(f'Select random id from list: {id_number}'):
            pass
        print('Nuber exercise on backend is: ', id_number)
        return payloads

    # General methods
    @staticmethod
    @allure.step('get_list_of_words_from_card_default')
    def get_list_of_words_from_card_default(card_id):
        result_post = requests.post(f'{Links.URL_MAIN_PAGE}api/tasks/{str(card_id)}',
                                    headers={'Content-Type': 'application/json',
                                             'Authorization': 'Bearer {}'.format(id_token_default)})
        with allure.step(f'Status code is: {result_post.status_code}'):
            pass
        amount_words = len(json.loads(result_post.text)['data']["answerOptions"])
        words = [json.loads(result_post.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    @staticmethod
    @allure.step('get_random_id_from_payloads')
    def get_random_id_from_payloads(payloads):
        exercises = requests.post(f'{Links.URL_MAIN_PAGE}api/exercises/byIds',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token_default)}, json=payloads)
        random_id = random.choice(exercises.json()['data'])
        print('random_id', random_id)
        return random_id
