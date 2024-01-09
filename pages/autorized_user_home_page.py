from locators.authotised_user_home_page_locators import AuthorizedUserHomePageLocators
from pages.base_page import BasePage


class AuthorizedUserHomePage(BasePage):
    locators = AuthorizedUserHomePageLocators()

    def click_speech_exercises(self):
        self.element_is_present_and_clickable(self.locators.EN_BUTTON).click()
        self.element_is_present_and_clickable(self.locators.SPEECH_EXERCISES_EN).click()
        self.element_is_present_and_clickable(self.locators.WORDS_BUTTON).click()

