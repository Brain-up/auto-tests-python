import os


class Data:
    DEFAULT_USER_1 = {'login': 'default@default.ru', 'password': 'password'}
    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")
