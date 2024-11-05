"""Methods for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
from pages.base_page import BasePage
from locators.exercises_words_ru_page_locators import ExercisesWordsRuPageLocators


class ExercisesWordsRuPage(BasePage):
    locators = ExercisesWordsRuPageLocators
    pass
