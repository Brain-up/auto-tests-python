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

    @allure.step("Get structure of section 1 with content on the page")
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
    def get_structure_of_2nd_level_in_section(self):
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

    @allure.step("Get structure of subsections on the page")
    def get_structure_of_3rd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_SECOND_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 2nd level of nesting in the section is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 2nd level of nesting in the section are: {tags}")
        return tags

    @allure.step("Check if elements on the 3rd level of nesting are visible on the page")
    def check_visibility_of_elements_on_3rd_level_in_section(self):
        elements = self.elements_are_present(self.locators.SECTION_SECOND_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()



