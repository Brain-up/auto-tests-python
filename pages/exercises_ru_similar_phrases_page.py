"""Methods for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
from pages.base_page import BasePage
from locators.exercises_ru_similar_phrases_page_locators import ExercisesRuSimilarPhrasesPageLocators


class ExercisesRuSimilarPhrasesPage(BasePage):
    locators = ExercisesRuSimilarPhrasesPageLocators
