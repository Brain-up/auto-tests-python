"""Locators of web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from selenium.webdriver.common.by import By


class ExercisesRuSimilarPhrasesPageLocators:
    PAGE_CONTENT = (By.TAG_NAME, "main")
    PAGE_FIRST_LEVEL_ELEMENTS = (By.XPATH, "//main/*")
