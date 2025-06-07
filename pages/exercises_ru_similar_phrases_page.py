"""Methods for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
import allure
import requests
from pages.base_page import BasePage
from locators.exercises_ru_similar_phrases_page_locators import ExercisesRuSimilarPhrasesPageLocators


class ExercisesRuSimilarPhrasesPage(BasePage):
    locators = ExercisesRuSimilarPhrasesPageLocators

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
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Get structure of the 7th level of nesting on the page")
    def get_structure_of_7th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SEVENTH_LEVEL_ELEMENTS)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check if elements of the 7th level of nesting are visible")
    def check_elements_visibility_on_7th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_7th_level())

    @allure.step("Check the list1 on the 5th level of nesting is present on the page")
    def get_list1_of_breadcrumbs_links(self):
        elements = self.elements_are_present(self.locators.PAGE_LIST1)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check the list1 is visible")
    def check_list1_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST1)

    @allure.step("Check the list2 on the 5th level of nesting is present on the page")
    def get_list2_of_group_links(self):
        elements = self.elements_are_present(self.locators.PAGE_LIST2)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check the list2 is visible")
    def check_list2_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST2)

    @allure.step("Check the list3 on the 5th level of nesting is present on the page")
    def get_list3_of_subgroup_links(self):
        elements = self.elements_are_present(self.locators.PAGE_LIST3)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check the list3 is visible")
    def check_list3_visibility(self):
        return all(element.is_displayed() for element in self.get_list3_of_subgroup_links())

    @allure.step("Check the list4 on the 6th level of nesting is present on the page")
    def get_list4_of_links(self):
        elements = self.elements_are_present(self.locators.CARD_IMAGES_LIST4)
        tags = [element.tag_name for element in elements]
        # print(*tags)
        return elements

    @allure.step("Check the list4 is visible")
    def check_list4_visibility(self):
        return all(element.is_displayed() for element in self.get_list4_of_links())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        tab_title = self.get_current_tab_title()
        return tab_title

    @allure.step("Get value of the breadcrumbs on the page")
    def get_value_of_breadcrumbs(self):
        breadcrumbs_text = [element.text for element in self.get_list1_of_breadcrumbs_links()]
        # print(len(breadcrumbs_text), breadcrumbs_text, sep='\n')
        return breadcrumbs_text

    @allure.step("Get text in group links on the page")
    def get_group_links_text(self):
        links_text = [element.text for element in self.get_list2_of_group_links()]
        # print(len(links_text), *links_text, sep='\n')
        return links_text

    @allure.step("Get text in subgroup links on the page")
    def get_subgroup_links_text(self):
        subgroup_links_text = [element.text for element in self.get_list3_of_subgroup_links()]
        # print(len(subgroup_links_text), subgroup_links_text, sep='\n')
        return subgroup_links_text

    # Checking links on the page
    @allure.step("Check if breadcrumbs are clickable")
    def check_breadcrumbs_clickability(self):
        return all(link.is_enabled() for link in self.get_list1_of_breadcrumbs_links())

    @allure.step("Get attribute 'href' of links in breadcrumbs")
    def get_breadcrumbs_links_href(self):
        breadcrumbs_links_href = [element.get_attribute("href") for element in self.get_list1_of_breadcrumbs_links()]
        # print(len(breadcrumbs_links_href), *breadcrumbs_links_href, sep='\n')
        return breadcrumbs_links_href

    @allure.step("Get status code of links in breadcrumbs")
    def get_link_status_codes_in_breadcrumbs(self):
        return [requests.head(link_href).status_code for link_href in self.get_breadcrumbs_links_href()]

    @allure.step("Check if group links are clickable")
    def check_group_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list2_of_group_links())

    @allure.step("Get attribute 'title' of group links")
    def get_group_link_titles(self):
        group_link_titles = [element.get_attribute("title") for element in self.get_list2_of_group_links()]
        # print(len(group_link_titles), *group_link_titles, sep='\n')
        return group_link_titles

    @allure.step("Get attribute 'active-links' of group links")
    def get_group_link_active_links(self):
        group_link_active_links = [el.get_attribute("data-test-active-link") for el in self.get_list2_of_group_links()]
        # print(len(group_link_active_links), *group_link_active_links, sep='\n')
        return group_link_active_links
