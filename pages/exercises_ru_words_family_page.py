"""Methods for verifying web elements on the exercises subgroup "Family" page
in the series "Words" on the "ru" local"""
import allure
from pages.base_page import BasePage
from locators.exercises_ru_words_family_page_locators import ExercisesRuWordsFamilyPageLocators


class ExercisesRuWordsFamilyPage(BasePage):
    locators = ExercisesRuWordsFamilyPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)
