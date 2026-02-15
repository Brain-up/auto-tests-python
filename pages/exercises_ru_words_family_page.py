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

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level(self):
        return self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        return self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        return self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        return self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        return self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        return self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Get structure of the 7th level of nesting on the page")
    def get_structure_of_7th_level(self):
        return self.elements_are_present(self.locators.PAGE_SEVENTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 7th level of nesting are visible")
    def check_elements_visibility_on_7th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_7th_level())

    @allure.step("Get structure of the 8th level of nesting on the page")
    def get_structure_of_8th_level(self):
        return self.elements_are_present(self.locators.PAGE_EIGHTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 8th level of nesting are visible")
    def check_elements_visibility_on_8th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_8th_level())

    def check_elements_invisibility_on_8th_level(self):
        return all(not el.is_displayed() for el in self.driver.find_elements(*self.locators.PAGE_EIGHTH_LEVEL_ELEMENTS))

    @allure.step("Get structure of the 9th level of nesting on the page")
    def get_structure_of_9th_level(self):
        return self.elements_are_present(self.locators.PAGE_NINTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 9th level of nesting are visible")
    def check_elements_visibility_on_9th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_9th_level())

    @allure.step("Get structure of the 10th level of nesting on the page")
    def get_structure_of_10th_level(self):
        return self.elements_are_present(self.locators.PAGE_TENTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 10th level of nesting are visible")
    def check_elements_visibility_on_10th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_10th_level())

    @allure.step("Get structure of the 11th level of nesting on the page")
    def get_structure_of_11th_level(self):
        return self.elements_are_present(self.locators.PAGE_ELEVENTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 11th level of nesting are visible")
    def check_elements_visibility_on_11th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_11th_level())

    @allure.step("Get structure of the 12th level of nesting on the page")
    def get_structure_of_12th_level(self):
        return self.elements_are_present(self.locators.PAGE_TWELFTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 12th level of nesting are visible")
    def check_elements_visibility_on_12th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_12th_level())

    @allure.step("Get structure of the 13th level of nesting on the page")
    def get_structure_of_13th_level(self):
        return self.elements_are_present(self.locators.PAGE_THIRTEENTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 13th level of nesting are visible")
    def check_elements_visibility_on_13th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_13th_level())

    @allure.step("Get structure of the 14th level of nesting on the page")
    def get_structure_of_14th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTEENTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        # print(*tags, len(tags), sep='\n')
        return elements

    @allure.step("Check if elements of the 14th level of nesting are visible")
    def check_elements_visibility_on_14th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_14th_level())

    @allure.step("Check the list1 on the 5th level of nesting is present on the page")
    def get_list1_of_breadcrumbs_links(self):
        elements = self.elements_are_present(self.locators.PAGE_LIST1)
        att = [element.get_attribute("href") for element in elements]
        print(*att, len(att), sep='\n')
        return elements
