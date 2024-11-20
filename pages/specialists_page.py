"""Methods for verifying web elements on the 'Specialists' page"""
import time
import allure
import requests
from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.specialists_page_locators import SpecialistsPageLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from selenium.common import TimeoutException


class SpecialistsPage(BasePage):
    locators = SpecialistsPageLocators
    locators1 = StartUnauthorizedPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Open the 'Specialists' page")
    def open_specialists_page(self):
        self.driver.get(MainPageLinks.URL_SPECIALISTS_PAGE)

    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Check the title on the 2nd level of nesting is present on the page")
    def check_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the title on the 2nd level of nesting is visible")
    def check_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Check the page text on the 2nd level of nesting is present on the page")
    def check_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the text on the 2nd level of nesting is visible")
    def check_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step("Check the grid of specialist cards on the 2nd level of nesting is present on the page")
    def check_grid_presence(self):
        return self.element_is_present(self.locators.PAGE_GRID)

    @allure.step("Check the grid of specialists cards on the 2nd level of nesting is visible")
    def check_grid_visibility(self):
        return self.element_is_visible(self.locators.PAGE_GRID)

    @allure.step("Check the 'All Specialists' link on the 3rd level of nesting is present on the page")
    def check_all_specialists_link_presence(self):
        return self.element_is_present(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Check the 'All Specialists' link on the 3rd level of nesting is visible")
    def check_all_specialists_link_visibility(self):
        return self.element_is_visible(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Get the list of specialist cards on the 3rd level of nesting on the page")
    def get_list_of_cards(self):
        return self.elements_are_present(self.locators.SPECIALIST_CARDS)

    @allure.step("Check specialists cards on the 3rd level of nesting are visible")
    def check_cards_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_cards())

    @allure.step("Get the list of images in specialist cards on the 5th level of nesting on the page")
    def get_list_of_card_images(self):
        return self.elements_are_present(self.locators.CARD_IMAGES)

    @allure.step("Check the image in each specialist card is visible")
    def check_image_visibility_in_cards(self):
        time.sleep(5)
        try:
            card_images_visibility = all(element.is_displayed() for element in self.get_list_of_card_images())
            return card_images_visibility
        except TimeoutException:
            print("The entire set of images has not been loaded during the allotted time")
            return None

    @allure.step("Get the list of names in specialist cards on the 5th level of nesting on the page")
    def get_list_of_names_in_cards(self):
        return self.elements_are_present(self.locators.SPECIALIST_NAMES)

    @allure.step("Check a name in each specialist card is visible")
    def check_visibility_of_names_in_cards(self):
        return all(element.is_displayed() for element in self.get_list_of_names_in_cards())

    @allure.step("Get the list of professions in specialist cards on the 6th level of nesting on the page")
    def get_list_of_professions_in_cards(self):
        return self.elements_are_present(self.locators.SPECIALIST_PROFESSIONS)

    @allure.step("Check a profession in each specialist card is visible")
    def check_visibility_of_professions_in_cards(self):
        return all(element.is_displayed() for element in self.get_list_of_professions_in_cards())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title with tag 'h2' on the page")
    def get_value_of_page_title(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Get the list of name values in specialist cards on the page")
    def get_name_values_in_cards(self):
        return [name.text for name in self.get_list_of_names_in_cards()]

    @allure.step("Get the list of profession values in specialist cards on the page")
    def get_profession_values_in_cards(self):
        return [profession.text for profession in self.get_list_of_professions_in_cards()]

    @allure.step("Get text in the 'All Specialists' link")
    def get_text_in_all_specialists_link(self):
        return self.get_text(self.locators.ALL_SPECIALISTS_LINK)

    # Checking the 'All Specialists' link
    @allure.step("Check the 'All Specialists' link is clickable")
    def check_all_specialists_link_clickability(self):
        return self.element_is_clickable(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Get attribute 'href' of the 'All Specialists' link")
    def get_all_specialists_link_href(self):
        return self.get_link_href(self.locators.ALL_SPECIALISTS_LINK)

    @allure.step("Get status code of the 'All Specialists' link")
    def get_all_specialists_link_status_code(self):
        return requests.head(self.get_all_specialists_link_href()).status_code

    @allure.step("Click on the 'All Specialists' link and thereby open the corresponding web page in a new tab")
    def click_all_specialists_link(self):
        self.element_is_present_and_clickable(self.locators.ALL_SPECIALISTS_LINK).click()
        self.switch_to_new_window()
        return self.get_current_tab_url()

    @allure.step("Get text of the element on the Start Unauthorized page")
    def get_element_text_on_new_tab(self):
        return self.get_text(self.locators1.SECTION_1_TEXT)

    # Checking images in the grid
    @allure.step("Get the list of attribute 'src' values of images in specialist cards")
    def get_images_src(self):
        return [image.get_attribute('src') for image in self.get_list_of_card_images()]

    @allure.step("Get the list of attribute 'alt' values of images in specialist cards")
    def get_images_alt(self):
        return [image.get_attribute('alt') for image in self.get_list_of_card_images()]

    @allure.step("Get the list of sizes of images in specialist cards")
    def get_images_sizes(self):
        return [image.size for image in self.get_list_of_card_images()]

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images1(self):
        images = self.get_list_of_card_images()
        images_sizes_before = [image.size for image in images]
        # self.driver.set_window_size(1200, 800)
        self.driver.set_window_size(220, 700)
        images_sizes_after = [image.size for image in images]
        changed, lost, unchanged = [], [], []
        for i in range(len(images)):
            changed.append(i) if images_sizes_before[i] != images_sizes_after[i] else unchanged.append(i)
            lost.append(i) if images_sizes_after[i] == {'height': 0, 'width': 0} else None
        print('All images have changed sizes' if len(changed) == len(images) else 'Not all images have changed sizes')
        return changed

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images2(self):
        time.sleep(3)
        images = self.get_list_of_card_images()
        images_sizes_before = [image.size for image in images]
        self.driver.set_window_size(400, 1080)
        time.sleep(7)
        try:
            images_sizes_after = [image.size for image in images]
            changed, lost, unchanged = [], [], []
            for i in range(len(images)):
                changed.append(i) if images_sizes_before[i] != images_sizes_after[i] else unchanged.append(i)
                lost.append(i) if images_sizes_after[i] == {'height': 0, 'width': 0} else None
            print(f'All images have changed sizes' if len(changed) == len(images)
                  else f'Images {unchanged} have unchanged sizes')
            return changed
        except TimeoutException:
            print("The entire set of images has not been loaded during the allotted time after resizing")

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images(self):
        images = self.get_list_of_card_images()
        images_sizes_before = [image.size for image in images]
        self.driver.set_window_size(200, 700)
        images_sizes_after = [image.size for image in images]
        changed, lost, unchanged = [], [], []
        for i in range(len(images)):
            changed.append(i) if images_sizes_before[i] != images_sizes_after[i] else unchanged.append(i)
            lost.append(i) if images_sizes_after[i] == {'height': 0, 'width': 0} else None
        # print(f'\nChanged: {len(changed)}, Lost: {len(lost)}, Unchanged: {len(unchanged)}')
        return changed, lost, unchanged
