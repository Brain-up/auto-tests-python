"""Methods for verifying web elements on the 'Groups' page"""
import time
import allure
import requests
from pages.base_page import BasePage
from locators.groups_page_locators import GroupsPageLocators


class GroupsPage(BasePage):
    locators = GroupsPageLocators

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
        time.sleep(1)
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Check the title h3 on the 2nd level of nesting is present on the page")
    def check_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the title h3 on the 2nd level of nesting is visible")
    def check_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get the list of tiles on the 2nd level of nesting on the page")
    def get_list_of_tiles(self):
        return self.elements_are_present(self.locators.PAGE_TILES)

    @allure.step("Check if tiles on the 2nd level of nesting are visible")
    def check_visibility_of_tiles(self):
        return all(element.is_displayed() for element in self.get_list_of_tiles())

    @allure.step("Get the list of images on the 6th level of nesting on the page")
    def get_list_of_images(self):
        return self.elements_are_present(self.locators.PAGE_IMAGES)

    @allure.step("Check if images on the 6th level of nesting are visible")
    def check_visibility_of_images(self):
        time.sleep(3)
        return all(element.is_displayed() for element in self.get_list_of_images())

    @allure.step("Get the list of subtitles on the 6th level of nesting on the page")
    def get_list_of_subtitles(self):
        return self.elements_are_present(self.locators.PAGE_SUBTITLES)

    @allure.step("Check if subtitles on the 6th level of nesting are visible")
    def check_visibility_of_subtitles(self):
        return all(element.is_displayed() for element in self.get_list_of_subtitles())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title with tag 'h3' on the page")
    def get_value_of_page_title(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Get the list of subtitle 'h4' values on the page")
    def get_values_of_subtitles(self):
        return [subtitle.text for subtitle in self.get_list_of_subtitles()]

    # Checking links on the page
    @allure.step("Get the list of links on the 3rd level of nesting on the page")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.PAGE_LINKS)

    @allure.step("Check if links on the 3rd level of nesting are visible")
    def check_visibility_of_links(self):
        return all(element.is_displayed() for element in self.get_list_of_links())

    @allure.step("Check if links are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links")
    def get_links_href(self):
        time.sleep(1)
        links_href = [element.get_attribute("href") for element in self.get_list_of_links()]
        print(links_href)
        return links_href

    @allure.step("Get status code of links")
    def get_links_status_codes(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href()]

    @allure.step("Click on links on the page and thereby open corresponding web pages in the same tab")
    def click_on_links(self):
        opened_pages = []
        self.element_is_present_and_clickable(self.locators.PAGE_LINKS1).click()
        time.sleep(2)
        opened_pages.append(self.get_current_tab_url())
        print(self.get_current_tab_url())
        self.driver.back()
        time.sleep(2)
        self.element_is_present_and_clickable(self.locators.PAGE_LINKS2).click()
        time.sleep(3)
        opened_pages.append(self.get_current_tab_url())
        print(self.get_current_tab_url())
        print(opened_pages)
        self.driver.back()
        time.sleep(2)
        return opened_pages
