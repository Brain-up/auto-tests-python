import os
import allure
import requests
from dotenv import load_dotenv
from test_data.links import MainPageLinks as Links

load_dotenv()


class BrainUPAPI:

    @staticmethod
    @allure.step("Get user's token")
    def get_user_token(user_email, user_password):
        auth_url = os.environ["AUTH_URL"]
        user = {"email": user_email, "password": user_password, "returnSecureToken": "true"}
        response = requests.post(auth_url, user)
        token = response.json()['idToken']
        return token

    @staticmethod
    @allure.step('Delete authorised user')
    def delete_authorised_user(user_email, user_token):
        url = f'{Links.URL_MAIN_PAGE}{os.environ["DELETE_USER"]}{user_email}'
        headers = {'Authorization': f'Bearer {user_token}'}
        response = requests.delete(url=url, headers=headers)
        return response.status_code
