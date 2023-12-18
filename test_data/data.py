import os


class Data:
    DEFAULT_USER_1 = {'login': 'default@default.ru', 'password': 'password'}  # default user with limited access
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")


class FooterData:
    footer_elements_text_ru = {
        "CONTACT_US_LINK": "Обратная связь",
        "WITH_THE_SUPPORT_PHRASE": "При поддержке"
    }
