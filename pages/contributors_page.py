"""Methods for verifying web elements on the 'Contributors' page"""
import allure
import requests
from pages.base_page import BasePage
from locators.contributors_page_locators import ContributorsPageLocators
from test_data.contributors_page_data import ContributorsPageData


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
        return self.elements_are_present(self.locators.CARD_DESCRIPTIONS)

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
        # slogan = self.element_is_present(self.locators.PAGE_TEXT).text
        return self.element_is_present(self.locators.PAGE_TEXT).text

    @allure.step("Check the content of descriptions in cards")
    def check_values_of_card_descriptions(self):
        elements_with_text = self.elements_are_present(self.locators.CARD_DESCRIPTIONS)
        element_values = [element.text for element in elements_with_text]
        filled_count, empty_count = 0, 0
        for i in range(len(element_values)):
            if element_values[i]:
                filled_count += 1
            else:
                empty_count += 1
        common_count = filled_count + empty_count
        return common_count

    @allure.step("Check text in links in cards")
    def check_text_in_card_links(self):
        links = self.elements_are_present(self.locators.CARD_LINKS)
        element_values = [link.text for link in links]
        filled_count, empty_count = 0, 0
        for i in range(len(element_values)):
            if element_values[i]:
                filled_count += 1
            else:
                empty_count += 1
        common_count = filled_count + empty_count
        return common_count

    @allure.step("Check if links in the section are clickable")
    def check_links_clickability(self):
        links = self.get_list_of_links()
        all_links_are_enabled = all(link.is_enabled() for link in links)
        return all_links_are_enabled

    @allure.step("Get attribute 'href' of links in the section")
    def get_links_href(self):
        links = self.get_list_of_links()
        links_href = [element.get_attribute("href") for element in links]
        return links_href

    @allure.step("Get attribute 'href' of the 'All Team' link")
    def get_all_team_link_href(self):
        return self.get_link_href(self.locators.ALL_TEAM_LINK)

    @allure.step("Get status code of 'All Team' link")
    def get_all_team_link_status_code(self):
        link_href = self.get_all_team_link_href()
        link_status_code = requests.head(link_href).status_code
        return link_status_code

    @allure.step("Get text in the 'All Team' link")
    def get_text_in_all_team_link(self):
        return self.get_text(self.locators.ALL_TEAM_LINK)

    @allure.step("Check attribute 'src' of images in contributor cards on the page")
    def check_images_src_in_contributor_cards(self):
        card_images = self.elements_are_present(self.locators.CARD_IMAGES)
        src_list = [image.get_attribute('src') for image in card_images]
        image_src = [image_src.startswith(ContributorsPageData.images_src_start) for image_src in src_list]
        return image_src

    @allure.step("Get the list of attribute 'alt' values of images in contributor cards on the page")
    def get_images_alt_in_contributor_cards(self):
        card_images = self.elements_are_present(self.locators.CARD_IMAGES)
        alt_list = [image.get_attribute('alt') for image in card_images]
        return alt_list

    @allure.step("""Get the list of size values of images in contributor cards on the page 
                    and check their changes after resizing""")
    def check_size_changes_of_card_images(self):
        card_images = self.elements_are_present(self.locators.CARD_IMAGES)
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
                    # print(f"\n   The image #{i + 1} has sizes that changed: \nfrom {image_sizes_before[i]} before "
                    #       f"resizing \nto {image_sizes_after[i]} after resizing")
            else:
                unchanged += 1
                # print(f"\n   The image #{i + 1} has sizes that remain: \nthe same {image_sizes_before[i]} before resizing "
                #       f"\nand {image_sizes_after[i]} after resizing")
        # print(f"\nSummary of image size checks\n   Amount of images with changed sizes after resizing is: {changed}, "
        #       f"\nincluding images that have become invisible on the page: {lost}")
        # print(f"   Amount of images with unchanged sizes after resizing is: {unchanged}")
        return changed, lost, unchanged
