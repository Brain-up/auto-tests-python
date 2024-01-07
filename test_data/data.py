import os
import random
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


class Data:

    DEFAULT_USER_1 = {'login': 'autoTestSpecialist@brainup.spb.ru',
                      'password': 'password'}  # default user with limited access
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
    DEFAULT_USER_2 = {'login': 'default@default.ru', 'password': 'password'}  # default user with limited access
    FIRST_NAME = 'Auto Test'
    BIRTHDAY = random.randint(datetime.now().year - 100, datetime.now().year)
    EMAIL = f'autotest_N@{time.time()}.com'


class FooterData:
    footer_elements_text = {
        "CONTACT_US_LINK": ["Обратная связь", "Contact us"],
        "WITH_THE_SUPPORT_PHRASE": ["При поддержке", "With the support"]
    }

    footer_images_src = {
        "arasaac_img_src": "https://brainup.site/logos/logo_ARASAAC_black-6aced95542b919137b28bced5be83596.png",
        "epam_img_src": "https://brainup.site/logos/epam-cd401151c8ee5f14afbba10b72cd5fea.png",
        "jetbrains_img_src": "https://brainup.site/logos/jetbrains-variant-4_-fb6c06f46c4a6267ac60e84343940d8b.png",
        "reg_img_src": "https://brainup.site/logos/reg-ru.svg",
        "selectel_img_src": "https://brainup.site/logos/selectel-f49f7fdb2061466c4f28aa1e128bd9a4.png"
    }

    footer_images_alt = {
        "arasaac_img_alt": "ARASAAC",
        "epam_img_alt": "EPAM",
        "jetbrains_img_alt": "JetBrains",
        "reg_img_alt": "Регистратор доменных имен РЕГ.РУ",
        "selectel_img_alt": "Selectel"
    }


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

    test_data = 'title, first_name, birthday, email, password, confirm_password, error_message'
    DATA_REGISTRATION = [
        (
            'an existing email',
            Data.FIRST_NAME,
            Data.BIRTHDAY,
            os.environ["CHANGE_PASSWORD_EMAIL"],
            'password',
            'password',
            Messages.EXISTING_EMAIL
        ),
        (
            'new email and empty confirm password',
            Data.FIRST_NAME,
            Data.BIRTHDAY,
            Data.EMAIL,
            'password',
            '',
            Messages.EMPTY_CONFIRM_PASSWORD
        ),
        (
            'new email and empty password',
            Data.FIRST_NAME,
            Data.BIRTHDAY,
            Data.EMAIL,
            '',
            'password',
            Messages.EMPTY_PASSWORD
        ),
        (
            'new email and empty first name',
            '',
            Data.BIRTHDAY,
            Data.EMAIL,
            'password',
            'password',
            Messages.EMPTY_NAME
        ),
        (
            'new email and empty birthday',
            Data.FIRST_NAME,
            '',
            Data.EMAIL,
            'password',
            'password',
            Messages.EMPTY_BIRTHDAY
        ),
        (
            'new email and empty email',
            Data.FIRST_NAME,
            Data.BIRTHDAY,
            '',
            'password',
            'password',
            Messages.EMPTY_EMAIL
        )
    ]
