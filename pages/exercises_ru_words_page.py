"""Methods for verifying web elements on the 'Exercises "Words"' page on the 'ru' local"""
import time

import allure
from pages.base_page import BasePage
from locators.exercises_ru_words_page_locators import ExercisesRuWordsPageLocators


class ExercisesRuWordsPage(BasePage):
    locators = ExercisesRuWordsPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Get structure of the 7th level of nesting on the page")
    def get_structure_of_7th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SEVENTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        print(tags)
        return elements

    @allure.step("Check if elements of the 7th level of nesting are visible")
    def check_elements_visibility_on_7th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_7th_level())

    @allure.step("Check the list1 on the 3rd level of nesting is present on the page")
    def check_list1_presence(self):
        return self.element_is_present(self.locators.PAGE_LIST1)

    @allure.step("Check the list1 on the 3rd level level of nesting is visible")
    def check_list1_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST1)

    @allure.step("Check the list2 on the 5th level of nesting is present on the page")
    def check_list2_presence(self):
        elements = self.elements_are_present(self.locators.PAGE_LIST2)
        # tags = [element.tag_name for element in elements]
        tags = [element.text for element in elements]
        print(tags)
        print(len(tags))
        return elements

    @allure.step("Check the list2 on the 5th level level of nesting is visible")
    def check_list2_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST2)

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()
