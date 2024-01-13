import allure

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.base_page import BasePage


class SpeechExercisesPage(BasePage):
    locators = SpeechExercisesPageLocators()

    def click_family_card(self):
        with allure.step('Click button "Family card"'):
            self.element_is_present_and_clickable(self.locators.FAMILY_CARD_EN).click()
