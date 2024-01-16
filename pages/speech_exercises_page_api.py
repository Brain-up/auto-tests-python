import json
import random

import allure
import requests

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.base_page import BasePage

authorization_url = ('https://www.googleapis.com/identitytoolkit/v3/'
                     'relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY')
data_default_user = {"email": "autoTestSpecialist@brainup.spb.ru", "password": "password",
                     "returnSecureToken": "true"}
result_post = requests.post(authorization_url, data_default_user)
id_token = json.loads(result_post.text)['idToken']
print(id_token)


class SpeechExercisesAPI(BasePage):
    locators = SpeechExercisesPageLocators()

    @staticmethod
    def get_random_id_from_list_sub_group_cards(card_id):
        list_cards_id = requests.get('https://brainup.site/api/subgroups?seriesId=9',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token)})
        result_get = json.loads(list_cards_id.text)
        print(result_get['data'])
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        print(id_number)
        return random.choice(result_get['data'][card_id]['exercises'])

    @staticmethod
    def get_random_id_from_list_sub_group_similar_cards(card_id):
        list_cards_id = requests.get('https://brainup.site/api/subgroups?seriesId=10',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token)})
        result_get = json.loads(list_cards_id.text)
        print(result_get)
        id_number = random.choice(result_get['data'][card_id]['exercises'])
        print(
            f'Random card from selected sub_group where level == card_id + 1, '
            f'it is mean current id {card_id} + 1 will be equal {card_id + 1}.\n',
            'ID exercise on the backend is: ', id_number,
            '\nThat is, we take a list of exercises on the back, and choose one exercise from it.')
        return id_number

    @staticmethod
    def get_list_of_words_from_card(card_id):
        result_get = requests.get(f'https://brainup.site/api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        word = json.loads(result_get.text)['data']["answerOptions"][0]['word']
        amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
        words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        with allure.step(f'Getting a list of exercise words from the backend: {words}.'):
            print('\nBACKEND LIST: ', words)
            ref_list = [i.lower() for i in words]
            print('\nBACKEND LIST in lowercase: ', ref_list)
        return ref_list

    def click_start_and_get_list_words(self):
        with allure.step('Click button "Start".'):
            self.element_is_present_and_clickable(self.locators.BUTTON_START).click()
        list_words = self.elements_are_visible(self.locators.LIST_WORDS_IN_CARD)
        words = [i.text.lower() for i in list_words]
        with allure.step(f'Getting a list of exercise words from the front: {words}'):
            print('\nUI LIST: ', words)
        return words
