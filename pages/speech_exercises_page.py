import allure

from locators.speech_exercises_page_locators import SpeechExercisesPageLocators
from pages.base_page import BasePage


class SpeechExercisesPage(BasePage):
    locators = SpeechExercisesPageLocators()

    def click_family_card(self):
        with allure.step('Click button "Family card"'):
            self.element_is_present_and_clickable(self.locators.FAMILY_CARD_EN).click()

    def check_button_interact(self):
        with allure.step('Check button "INTERACT" is present.'):
            button_interact = self.element_is_present_and_clickable(self.locators.BUTTON_INTERACT)
        with allure.step('Click button "INTERACT".'):
            button_interact.click()
            print('Clicked button INTERACT.')
            return button_interact

    def check_button_solve(self):
        with allure.step('Check button "SOLVE" is present.'):
            button_solve = self.element_is_present_and_clickable(self.locators.BUTTON_SOLVE)
        with allure.step('Click button "SOLVE".'):
            button_solve.click()
            print('Clicked button SOLVE.')
            return button_solve

    def check_progressbar(self):
        with allure.step('Check "progress-bar" is present after click button "SOLVE".'):
            progress_bar = self.elements_are_visible(self.locators.PROGRESS_BAR)
            return progress_bar
