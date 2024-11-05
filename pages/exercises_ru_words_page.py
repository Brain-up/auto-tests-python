"""Methods for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
from pages.base_page import BasePage
from locators.exercises_ru_words_page_locators import ExercisesRuWordsPageLocators


class ExercisesRuWordsPage(BasePage):
    locators = ExercisesRuWordsPageLocators
    pass
