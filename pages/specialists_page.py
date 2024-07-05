"""Methods for verifying web elements on the 'Specialists' page"""
import allure
import requests
from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.specialists_page_locators import SpecialistsPageLocators
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait
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
    def check_title_h2_presence(self):
        return self.element_is_present(self.locators.TITLE_H2)

    @allure.step("Check the title on the 2nd level of nesting is visible")
    def check_title_h2_visibility(self):
        return self.element_is_visible(self.locators.TITLE_H2)

    @allure.step("Check the page text on the 2nd level of nesting is present on the page")
    def check_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the text on the 2nd level of nesting is visible")
    def check_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step("Check the grid of specialist cards on the 2nd level of nesting is present on the page")
    def check_grid_presence(self):
        return self.element_is_present(self.locators.PAGE_GRID)

    @allure.step("Check the grid of specialists cards on the 2nd level of nesting is visible on the page")
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
        return len(self.elements_are_present(self.locators.SPECIALIST_CARDS))

    @allure.step("Check specialists cards on the 3rd level of nesting are visible on the page")
    def check_cards_visibility(self):
        cards = self.elements_are_present(self.locators.SPECIALIST_CARDS)
        return all(element.is_displayed() for element in cards)

    @allure.step("Get the list of images in specialist cards on the 5th level of nesting on the page")
    def get_list_of_card_images(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        return card_images

    @allure.step("Check the image in each specialist card is visible")
    def check_image_visibility_in_cards(self):
        try:
            card_images = (Wait(self.driver, 35).
                           until(ec.presence_of_all_elements_located(self.locators.GRID_CARD_IMAGES)))
            return all(element.is_displayed() for element in card_images)
        except TimeoutException:
            return False

    @allure.step("Get the list of names in specialist cards on the 5th level of nesting on the page")
    def get_list_of_names_in_cards(self):
        return self.elements_are_present(self.locators.SPECIALIST_NAMES)

    @allure.step("Check a name in each specialist card is visible")
    def check_visibility_of_names_in_cards(self):
        names = self.get_list_of_names_in_cards()
        return all(element.is_displayed() for element in names)

    @allure.step("Get the list of professions in specialist cards on the 6th level of nesting on the page")
    def get_list_of_professions_in_cards(self):
        return self.elements_are_present(self.locators.SPECIALIST_PROFESSIONS)

    @allure.step("Check a profession in each specialist card is visible")
    def check_visibility_of_professions_in_cards(self):
        professions = self.get_list_of_professions_in_cards()
        return all(element.is_displayed() for element in professions)

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title with tag 'h2' on the page")
    def get_value_of_title_h2(self):
        return self.get_text(self.locators.TITLE_H2)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Get the list of name values in specialist cards on the page")
    def get_name_values_in_cards(self):
        specialist_names = self.get_list_of_names_in_cards()
        return [name.text for name in specialist_names]

    @allure.step("Get the list of profession values in specialist cards on the page")
    def get_profession_values_in_cards(self):
        specialist_professions = self.get_list_of_professions_in_cards()
        return [profession.text for profession in specialist_professions]

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
    @allure.step("Get the list of attribute 'src' values of images in specialist cards on the page")
    def get_images_src_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        src_list = [image.get_attribute('src') for image in card_images]
        # print(f"The attribute 'src' values of images in cards on the page are:", *src_list, sep='\n')
        return src_list

    @allure.step("Get the list of attribute 'alt' values of images in specialist cards on the page")
    def get_images_alt_in_specialist_cards(self):
        card_images = self.get_list_of_card_images()
        alt_list = [image.get_attribute('alt') for image in card_images]
        # print(f"The attribute 'alt' values of images in cards on the page are:", *alt_list, sep='\n')
        return alt_list

    @allure.step("""Get the list of size values of images in specialist cards on the page 
                    and check their changes after resizing""")
    def check_size_changes_of_card_images(self):
        card_images = self.get_list_of_card_images()
        image_sizes_before = [image.size for image in card_images]
        self.driver.set_window_size(1200, 800)
        image_sizes_after = [image.size for image in card_images]
        # print("The results of checking changes of image sizes in cards after resizing are:")
        changed, lost, unchanged = 0, 0, 0
        for i in range(len(image_sizes_after)):
            if image_sizes_before[i] != image_sizes_after[i]:
                changed += 1
                if image_sizes_after[i] == {'height': 0, 'width': 0}:
                    lost += 1
                    # print(f"\n   The image #{i + 1} has become invisible because has sizes that changed: "
                    #       f"\nfrom {image_sizes_before[i]} before resizing \nto {image_sizes_after[i]} after resizing")
                # else:
                #     print(f"\n   The image #{i + 1} has sizes that changed: \nfrom {image_sizes_before[i]} before "
                #           f"resizing \nto {image_sizes_after[i]} after resizing")
            else:
                unchanged += 1
                # print(f"\n   The image #{i + 1} has sizes that remain: \nthe same {image_sizes_before[i]} before resizing "
                #       f"\nand {image_sizes_after[i]} after resizing")
        # print(f"\nSummary of image size checks\n   Amount of images with changed sizes after resizing is: {changed}, "
        #       f"\nincluding images that have become invisible on the page: {lost}")
        # print(f"   Amount of images with unchanged sizes after resizing is: {unchanged}")
        return changed, lost, unchanged

    @allure.step("Check the image is present in the 1th card")
    def check_the_1th_card_image_presence(self):
        return self.element_is_present(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Check the image is visible in the 1th card")
    def check_the_1th_card_image_visibility(self):
        return self.element_is_visible(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get attribute 'src' of the image in the 1th card")
    def get_the_1th_card_image_src(self):
        return self.get_image_src(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get attribute 'alt' of the image in the 1th card")
    def get_the_1th_card_image_alt(self):
        return self.get_image_alt(self.locators.GRID_CARD_01_IMAGE)

    @allure.step("Get size of the image in the 1th card")
    def get_visible_size_of_the_1th_card_image(self):
        image_size = self.get_image_size(self.locators.GRID_CARD_01_IMAGE)
        return image_size
