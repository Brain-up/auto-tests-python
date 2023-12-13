from locators.locators import AuthorizedUserHomePageLocators
from pages.base_page import BasePage


class AuthorizedUserHomePage(BasePage):
    locators = AuthorizedUserHomePageLocators()

    def click_speech_exercises(self):
        self.element_is_presence_and_clickable(self.locators.SPEECH_EXERCISES).click()

