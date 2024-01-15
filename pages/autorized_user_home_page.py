import time

import allure

from locators.authotised_user_home_page_locators import AuthorizedUserHomePageLocators
from pages.base_page import BasePage


class AuthorizedUserHomePage(BasePage):
    locators = AuthorizedUserHomePageLocators()

    def click_speech_exercises(self):
        with allure.step('Select English language. Click "EN" button.'):
            self.element_is_present_and_clickable(self.locators.EN_BUTTON).click()
        with allure.step('Click button "Speech exercises".'):
            self.element_is_present_and_clickable(self.locators.SPEECH_EXERCISES_EN).click()
        with allure.step('Click button "Words".'):
            self.element_is_present_and_clickable(self.locators.WORDS_BUTTON).click()

    def click_speech_exercises_01(self):
        with allure.step('Select English language. Click "EN" button.'):
            self.element_is_present_and_clickable(self.locators.EN_BUTTON).click()
        with allure.step('Click button "Speech exercises".'):
            self.element_is_present_and_clickable(self.locators.SPEECH_EXERCISES_EN).click()
