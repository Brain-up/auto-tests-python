from locators.locators import SpeechExercisesPageLocators
from pages.base_page import BasePage


class SpeechExercisesPage(BasePage):
    locators = SpeechExercisesPageLocators()

    def click_family_card(self):
        self.element_is_presence_and_clickable(self.locators.FAMILY_CARD).click()
