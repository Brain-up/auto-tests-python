import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class Messages:

    WRONG_PASSWORD = 'Error: The password is invalid or the user does not have a password.'
    WRONG_USER = 'Error: There is no user record corresponding to this identifier. The user may have been deleted.'
    EXISTING_EMAIL = 'The email address is already in use by another account.'
    EMPTY_CONFIRM_PASSWORD = ['Passwords should match', 'Пароли должны совпадать']
    EMPTY_NAME = ['Empty LastName', 'Фамилия не Указана']
    EMPTY_BIRTHDAY = ['Invalid date', 'Некорректная дата']
    EMPTY_GENDER = ['Empty gender', 'Пол не указан']
    EMPTY_EMAIL = ['Please enter your login and password', 'Пожалуйста, введите логин и пароль.']
    EMPTY_PASSWORD = ['Passwords should match', 'Пароли должны совпадать']
    ONLY_FIRST_NAME = ['Empty LastName', 'Фамилия не Указана']


class Registration:
    FIRST_NAME = 'Auto Test'
    BIRTHDAY = random.randint(datetime.now().year - 100, datetime.now().year)
    EMAIL = f'autotestuser_n@{str(time.time()).replace(".", "")}.com'
    test_data = 'title, first_name, birthday, email, password, confirm_password, error_message'
    DATA_REGISTRATION = [
        (
            'an existing email',
            FIRST_NAME,
            BIRTHDAY,
            os.environ["CHANGE_PASSWORD_EMAIL"],
            'password',
            'password',
            Messages.EXISTING_EMAIL
        ),
        (
            'new email and empty confirm password',
            FIRST_NAME,
            BIRTHDAY,
            EMAIL,
            'password',
            '',
            Messages.EMPTY_CONFIRM_PASSWORD
        ),
        (
            'new email and empty password',
            FIRST_NAME,
            BIRTHDAY,
            EMAIL,
            '',
            'password',
            Messages.EMPTY_PASSWORD
        ),
        (
            'new email and empty first name',
            '',
            BIRTHDAY,
            EMAIL,
            'password',
            'password',
            Messages.EMPTY_NAME
        ),
        (
            'new email and empty birthday',
            FIRST_NAME,
            '',
            EMAIL,
            'password',
            'password',
            Messages.EMPTY_BIRTHDAY
        ),
        (
            'new email and empty email',
            FIRST_NAME,
            BIRTHDAY,
            '',
            'password',
            'password',
            Messages.EMPTY_EMAIL
        )
    ]
