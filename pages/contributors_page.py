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

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections_on_page(self):
        return len(self.elements_are_present(self.locators.PAGE_SECTIONS))

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get list of subsections on the 2nd level of nesting on the page")
    def get_list_of_subsections_on_2nd_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_SUBSECTIONS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check subsections are visible")
    def check_visibility_of_subsections_on_2nd_level_on_page(self):
        return all(subsection.is_displayed() for subsection in self.get_list_of_subsections_on_2nd_level_on_page())

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

    @allure.step("Get the list of subsections on the 4th level of nesting")
    def get_amount_of_subsections_on_4th_level(self):
        subsections = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_CONTAINERS)
        return len(subsections)

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Get amount of contributor's cards in the section grid")
    def get_amount_of_cards_in_the_grid(self):
        contributor_cards = self.elements_are_present(self.locators.GRID_CONTRIBUTOR_CARDS)
        return len(contributor_cards)

    @allure.step("Get amount of contributor's images in the section grid")
    def get_amount_of_images_in_the_grid(self):
        images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        return len(images)

    @allure.step("Get amount of contributor's links in the section grid")
    def get_amount_of_links_in_the_grid(self):
        links = self.elements_are_present(self.locators.GRID_CARD_LINKS)
        return len(links)

    @allure.step("Get amount of contributor's descriptions in the section grid")
    def get_amount_of_descriptions_in_the_grid(self):
        descriptions = self.elements_are_present(self.locators.GRID_CARD_DESCRIPTIONS)
        return len(descriptions)

    @allure.step("Get value of the subtitle in the section on the page")
    def get_value_of_title_on_the_page(self):
        title_value = self.get_text(self.locators.SECTION_TITLE)
        return title_value

    @allure.step("Get the list of subtitle values on the page")
    def get_values_of_subtitles(self):
        subtitles = self.elements_are_present(self.locators.SECTION_SUBTITLES)
        subtitle_values = [subtitle.text for subtitle in subtitles]
        return subtitle_values

    @allure.step("Get text in the slogan on the page")
    def get_value_of_slogan(self):
        slogan = self.element_is_present(self.locators.SLOGAN).text
        return slogan

    @allure.step("Check the content of descriptions in cards")
    def check_values_of_card_descriptions(self):
        elements_with_text = self.elements_are_present(self.locators.GRID_CARD_DESCRIPTIONS)
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
        links = self.elements_are_present(self.locators.GRID_CARD_LINKS)
        element_values = [link.text for link in links]
        filled_count, empty_count = 0, 0
        for i in range(len(element_values)):
            if element_values[i]:
                filled_count += 1
            else:
                empty_count += 1
        common_count = filled_count + empty_count
        return common_count

    @allure.step("Get the list of links in the section")
    def get_list_of_links_in_section(self):
        links = self.elements_are_present(self.locators.SECTION_LINKS)
        # print(f"\nAmount of links in the section is: {len(links)}")
        return links

    @allure.step("Check if links are visible in the section")
    def check_visibility_of_links_in_section(self):
        links = self.get_list_of_links_in_section()
        all_links_are_displayed = all(link.is_displayed() for link in links)
        return all_links_are_displayed

    @allure.step("Check if links in the section are clickable")
    def check_links_clickability(self):
        links = self.get_list_of_links_in_section()
        all_links_are_enabled = all(link.is_enabled() for link in links)
        return all_links_are_enabled

    @allure.step("Get attribute 'href' of links in the section")
    def get_links_href(self):
        links = self.get_list_of_links_in_section()
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

    @allure.step("Check the image in each contributor card is present and visible on the page")
    def check_image_presence_and_visibility_in_the_grid(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        all_images_are_displayed = all(image.is_displayed() for image in card_images)
        return all_images_are_displayed

    @allure.step("Check attribute 'src' of images in contributor cards on the page")
    def check_images_src_in_contributor_cards(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        src_list = [image.get_attribute('src') for image in card_images]
        image_src = [image_src.startswith(ContributorsPageData.images_src_start) for image_src in src_list]
        return image_src

    @allure.step("Get the list of attribute 'alt' values of images in contributor cards on the page")
    def get_images_alt_in_contributor_cards(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        alt_list = [image.get_attribute('alt') for image in card_images]
        return alt_list

    @allure.step("""Get the list of size values of images in contributor cards on the page 
                    and check their changes after resizing""")
    def check_size_changes_of_card_images(self):
        card_images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
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
