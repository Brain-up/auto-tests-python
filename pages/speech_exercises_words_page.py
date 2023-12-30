import json
import random

import requests

from locators.locators import SpeechExercisesPageLocators
from pages.base_page import BasePage

authorization_url = ('https://www.googleapis.com/identitytoolkit/v3/'
                     'relyingparty/verifyPassword?key=AIzaSyCxu7mVxd_waBDUn9VKblBl4zl8MX5WxWY')
data_default_user = {"email": "autoTestSpecialist@brainup.spb.ru", "password": "password",
                     "returnSecureToken": "true"}
result_post = requests.post(authorization_url, data_default_user)
id_token = json.loads(result_post.text)['idToken']
print(id_token)


class SpeechExercisesWordsPage(BasePage):
    locators = SpeechExercisesPageLocators()

    @staticmethod
    def get_random_id_from_list_all_family_cards():
        list_cards_id = requests.get('https://brainup.site/api/subgroups?seriesId=9',
                                     headers={'Content-Type': 'application/json',
                                              'Authorization': 'Bearer {}'.format(id_token)})
        result_get = json.loads(list_cards_id.text)
        # print(result_get['data'][0]['exercises'])
        return random.choice(result_get['data'][0]['exercises'])

    @staticmethod
    def get_list_of_words_from_card(card_id):
        print('Card id is:', card_id)
        result_get = requests.get(f'https://brainup.site/api/tasks/{str(card_id)}',
                                  headers={'Content-Type': 'application/json',
                                           'Authorization': 'Bearer {}'.format(id_token)})
        word = json.loads(result_get.text)['data']["answerOptions"][0]['word']
        amount_words = len(json.loads(result_get.text)['data']["answerOptions"])
        words = [json.loads(result_get.text)['data']["answerOptions"][i]['word'] for i in range(amount_words)]
        print(words)
        return words

    def click_start_and_get_list_words(self):
        self.element_is_presence_and_clickable(self.locators.BUTTON_START).click()
        list_words = self.elements_are_visible(self.locators.LIST_CARD_WORDS_WE)
        words = [i.text.lower() for i in list_words]
        print(words)
        return words
