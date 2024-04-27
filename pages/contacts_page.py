"""Methods for verifying web elements on the 'Contacts' page"""
import allure
from pages.base_page import BasePage
from locators.contacts_page_locators import ContactsPageLocators


class ContactsPage(BasePage):
    locators = ContactsPageLocators

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

    @allure.step("Check if elements of the 1st level are visible on the page")
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
    def get_structure_of_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 1st level of nesting in the section 1 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting in the section 1 are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level are visible in the section 1")
    def check_visibility_of_elements_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of section 2 with content on the page")
    def get_structure_of_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIRST_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 1st level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level are visible in the section 2")
    def check_visibility_of_elements_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIRST_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of subsections in section 2 with content on the page")
    def get_structure_of_2nd_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_SECOND_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 2nd level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 2nd level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible in the section 2")
    def check_visibility_of_elements_in_subsection_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_SECOND_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-subsections in section 2 with content on the page")
    def get_structure_of_3rd_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_THIRD_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 3rd level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 3rd level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 3rd level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_3rd_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_THIRD_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-sub-subsections in section 2 with content on the page")
    def get_structure_of_4th_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FOURTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 4th level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 4th level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 4th level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_4th_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FOURTH_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-sub-sub-subsections in section 2 with content on the page")
    def get_structure_of_5th_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIFTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 5th level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 5th level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 5th level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_5th_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIFTH_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()
