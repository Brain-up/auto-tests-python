"""Methods for verifying web elements on the 'Contributors' page"""
import allure
from pages.base_page import BasePage
from locators.contributors_page_locators import ContributorsPageLocators


class ContributorsPage(BasePage):
    locators = ContributorsPageLocators

    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the page")
    def get_structure_of_page(self):
        elements = self.elements_are_present(self.locators.PAGE_STRUCTURE)
        print(f"Amount of elements on the 1st level of nesting on the page is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting on the page are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level of nesting are visible on the page")
    def check_visibility_of_elements_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_STRUCTURE)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections_on_page(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        print(len(sections))
        return len(sections)

    @allure.step("Check sections are visible on the page")
    def check_visibility_of_sections(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        for section in sections:
            return section.is_displayed()

    @allure.step("Get structure of section with content on the page")
    def get_structure_of_section(self):
        elements = self.elements_are_present(self.locators.SECTION_FIRST_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 1st level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level are visible in the section")
    def check_visibility_of_elements_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_FIRST_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of subsections in the section")
    def get_structure_of_1st_level_in_section(self):
        elements = self.elements_are_present(self.locators.PAGE_SUBSECTIONS)
        print(f"Amount of subsections on the 1st level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of subsections on the 1st level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check subsections are visible in the section")
    def check_visibility_of_elements_in_subsections(self):
        subsections = self.elements_are_present(self.locators.PAGE_SUBSECTIONS)
        for subsection in subsections:
            return subsection.is_displayed()

    @allure.step("Get structure of sub-subsections on the page") #ch
    def get_structure_of_2nd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_SECOND_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 2nd level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 2nd level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check if elements on the 2nd level of nesting are visible on the page")
    def check_visibility_of_elements_on_2nd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_SECOND_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-sub-subsections on the page")
    def get_structure_of_3rd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_THIRD_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 3rd level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 3rd level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check if elements of the 3rd level of nesting are visible on the page")
    def check_visibility_of_elements_on_3rd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_THIRD_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get the list of subsections on the 3rd level of nesting")
    def get_amount_of_subsections_on_3rd_level(self):
        subsections = self.elements_are_present(self.locators.SECTION_THIRD_LEVEL_CONTAINERS)
        print(f"Amount of subsections on the 3rd level is: {len(subsections)}")
        return len(subsections)

    @allure.step("Get structure of elements of the 4th level of nesting")
    def get_structure_of_4th_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_FOURTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 4th level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 4th level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check if elements of the 4th level of nesting are visible on the page")
    def check_visibility_of_elements_on_4th_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_FOURTH_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get amount of contributor's cards in the section grid")
    def get_amount_of_cards_in_the_grid(self):
        contributor_cards = self.elements_are_present(self.locators.GRID_CONTRIBUTOR_CARDS)
        print(f"Amount of contributor cards in the grid is: {len(contributor_cards)}")
        return len(contributor_cards)

    @allure.step("Get amount of contributor's images in the section grid")
    def get_amount_of_images_in_the_grid(self):
        images = self.elements_are_present(self.locators.GRID_CARD_IMAGES)
        print(f"Amount of images in the grid is: {len(images)}")
        return len(images)

    @allure.step("Get amount of contributor's links in the section grid")
    def get_amount_of_links_in_the_grid(self):
        links = self.elements_are_present(self.locators.GRID_CARD_LINKS)
        print(f"Amount of links in the grid is: {len(links)}")
        return len(links)

    @allure.step("Get amount of contributor's descriptions in the section grid")
    def get_amount_of_descriptions_in_the_grid(self):
        descriptions = self.elements_are_present(self.locators.GRID_CARD_DESCRIPTIONS)
        print(f"Amount of descriptions in the grid is: {len(descriptions)}")
        return len(descriptions)

    @allure.step("Get value of the title in the section on the page")
    def get_value_of_title_on_the_page(self):
        title_value = self.get_text(self.locators.SECTION_TITLE)
        print(f"The title value on the page is: {title_value}")
        return title_value

    @allure.step("Get value of the subtitle in the section on the page")
    def get_value_of_title_on_the_page(self):
        title_value = self.get_text(self.locators.SECTION_TITLE)
        print(f"The title value on the page is: {title_value}")
        return title_value

    @allure.step("Get the list of subtitle values on the page")
    def get_values_of_subtitles(self):
        subtitles = self.elements_are_present(self.locators.SECTION_SUBTITLES)
        subtitle_values = [subtitle.text for subtitle in subtitles]
        print(f"The subtitle values on the page are:", *subtitle_values, sep='\n')
        return subtitle_values
