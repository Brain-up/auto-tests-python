"""Methods for verifying web elements on the 'Contributors' page"""
import allure
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from pages.base_page import BasePage
from locators.contributors_page_locators import ContributorsPageLocators


class ContributorsPage(BasePage):
    locators = ContributorsPageLocators

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

    @allure.step("Check the title h2 on the 2nd level of nesting is present on the page")
    def check_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the title h2 on the 2nd level of nesting is visible")
    def check_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get the list of subtitles h3 on the 2nd level of nesting on the page")
    def get_list_of_subtitles(self):
        return self.elements_are_present(self.locators.PAGE_SUBTITLES)

    @allure.step("Check if subtitles h3 on the 2nd level of nesting are visible")
    def check_visibility_of_subtitles(self):
        return all(element.is_displayed() for element in self.get_list_of_subtitles())

    @allure.step("Get the list of cards on the 3rd level of nesting on the page")
    def get_list_of_cards(self):
        return self.elements_are_present(self.locators.CONTRIBUTOR_CARDS)

    @allure.step("Check cards are visible")
    def check_cards_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_cards())

    @allure.step("Get the list of descriptions in cards on the 4th level of nesting on the page")
    def get_list_of_card_descriptions(self):
        return Wait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.locators.CARD_DESCRIPTIONS))

    @allure.step("Check descriptions in cards are visible")
    def check_descriptions_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_card_descriptions())

    @allure.step("Get the list of links on the 4th level of nesting on the page")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.PAGE_LINKS)

    @allure.step("Check links on the page are visible")
    def check_links_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_links())

    @allure.step("Get the list of images in cards on the 5th level of nesting on the page")
    def get_list_of_card_images(self):
        return self.elements_are_present(self.locators.CARD_IMAGES)

    @allure.step("Check images in cards are visible")
    def check_image_visibility_in_cards(self):
        return all(element.is_displayed() for element in self.get_list_of_card_images())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title h2 on the page")
    def get_value_of_title(self):
        return self.check_title_presence().text

    @allure.step("Get the list of subtitle h3 values on the page")
    def get_values_of_subtitles(self):
        return [subtitle.text for subtitle in self.get_list_of_subtitles()]

    @allure.step("Get content of the text on the page")
    def get_text_content_on_page(self):
        return self.element_is_present(self.locators.PAGE_TEXT).text

    @allure.step("Check the content of descriptions in cards")
    def check_values_of_card_descriptions(self):
        values = [element.text for element in self.get_list_of_card_descriptions()]
        full, empty = [], []
        for i in range(len(values)):
            full.append(values[i]) if values[i] else empty.append(values[i])
        return len(full) + len(empty)

    @allure.step("Check text in links in cards")
    def check_text_in_card_links(self):
        values = [link.text for link in self.elements_are_present(self.locators.CARD_LINKS)]
        full, empty = [], []
        for i in range(len(values)):
            full.append(values[i]) if values[i] else empty.append(values[i])
        return len(full) + len(empty)

    @allure.step("Get text in the 'All Team' link")
    def get_text_in_all_team_link(self):
        return self.element_is_present(self.locators.ALL_TEAM_LINK).text

    # Checking links on the page
    @allure.step("Check if links on the page are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links on the page")
    def get_links_href(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Get attribute 'href' of the 'All Team' link")
    def get_all_team_link_href(self):
        return self.get_link_href(self.locators.ALL_TEAM_LINK)

    @allure.step("Get status code of the 'All Team' link")
    def get_all_team_link_status_code(self):
        return requests.head(self.get_all_team_link_href()).status_code

    # Checking images in grids
    @allure.step("Get the list of attribute 'src' values of images in contributor cards")
    def get_images_src(self):
        return [image.get_attribute('src') for image in self.get_list_of_card_images()]

    @allure.step("Get the list of attribute 'alt' values of images in contributor cards")
    def get_images_alt(self):
        return [image.get_attribute('alt') for image in self.get_list_of_card_images()]

    @allure.step("Get the list of sizes of images in contributor cards")
    def get_images_sizes(self):
        return [image.size for image in self.get_list_of_card_images()]

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
