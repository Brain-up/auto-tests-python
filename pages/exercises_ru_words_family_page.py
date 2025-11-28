"""Methods for verifying web elements on the 'Exercises "Family"' page in the series "Words" on the 'ru' local"""
from pages.base_page import BasePage
from locators.exercises_ru_words_family_page_locators import ExercisesRuWordsFamilyPageLocators


class ExercisesRuWordsFamilyPage(BasePage):
    locators = ExercisesRuWordsFamilyPageLocators
