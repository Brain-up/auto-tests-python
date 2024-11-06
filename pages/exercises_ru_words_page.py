"""Methods for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
import allure
from pages.base_page import BasePage
from locators.exercises_ru_words_page_locators import ExercisesRuWordsPageLocators


class ExercisesRuWordsPage(BasePage):
    locators = ExercisesRuWordsPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)
