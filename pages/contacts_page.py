"""Methods for verifying web elements on the 'Contacts' page"""
import allure
import requests
from pages.base_page import BasePage
from locators.contacts_page_locators import ContactsPageLocators


class ContactsPage(BasePage):
    locators = ContactsPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting in the section 1")
    def get_structure_of_1st_level_in_section1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible in the section 1")
    def check_elements_visibility_on_1st_level_in_section1(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level_in_section1())

    @allure.step("Get structure of the 1st level of nesting in the section 2")
    def get_structure_of_1st_level_in_section2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible in the section 2")
    def check_elements_visibility_on_1st_level_in_section2(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level_in_section2())

    @allure.step("Get structure of the 2nd level of nesting in the section 2")
    def get_structure_of_2nd_level_in_section2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible in the section 2")
    def check_elements_visibility_on_2nd_level_in_section2(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level_in_section2())

    @allure.step("Get structure of the 3rd level of nesting in the section 2")
    def get_structure_of_3rd_level_in_section2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_3rd_level_in_section2(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level_in_section2())

    @allure.step("Get structure of the 4th level of nesting in the section 2")
    def get_structure_of_4th_level_in_section2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FOURTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 4th level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_4th_level_in_section2(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level_in_section2())

    @allure.step("Get structure of the 5th level of nesting in the section 2")
    def get_structure_of_5th_level_in_section2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 5th level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_5th_level_in_section2(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level_in_section2())

    @allure.step("Get structure of the page")
    def get_page_structure(self):
        elements = self.elements_are_present(self.locators.PAGE_STRUCTURE)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_visibility_of_structural_elements(self):
        return all(element.is_displayed() for element in self.get_page_structure())

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        return len(sections)

    @allure.step("Check if sections are visible")
    def check_visibility_of_sections(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        return all(element.is_displayed() for element in sections)

    @allure.step("Check if the dividing line is present on the page")
    def check_presence_of_dividing_line(self):
        return self.element_is_present(self.locators.PAGE_DIVIDING_LINE)

    @allure.step("Check if the dividing line is visible")
    def check_visibility_of_dividing_line(self):
        return self.element_is_visible(self.locators.PAGE_DIVIDING_LINE)

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title h1 on the page")
    def get_value_of_title_h1(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Get the list of subtitles h2 on the page")
    def get_list_of_subtitles_h2(self):
        return self.elements_are_present(self.locators.PAGE_SUBTITLES)

    @allure.step("Get the list of subtitle values")
    def get_values_of_subtitles_h2(self):
        subtitles = self.get_list_of_subtitles_h2()
        return [subtitle.text for subtitle in subtitles]

    @allure.step("Get the list of elements with text in sections 1, 2 on the page")
    def get_list_of_elements_with_text_in_sections(self):
        elements_with_text = self.elements_are_present(self.locators.SECTION_2_TEXT_PAR)
        # print(f"\nAmount of elements with text in sections 1, 2 is: {len(elements_with_text)}")
        return elements_with_text

    @allure.step("Get the list of text content in sections 1, 2 on the page")
    def get_values_of_text_in_sections(self):
        elements_with_text = self.get_list_of_elements_with_text_in_sections()
        element_values = [element.text for element in elements_with_text]
        # print(f"The content of the text in the sections 1, 2 is:", *element_values, sep='\n\n')
        return element_values

    @allure.step("Get the list of text content in sections 1, 2 on the page")
    def get_text_in_links_in_sections(self):
        links = self.elements_are_present(self.locators.SECTION_2_LINKS)
        links_text = [link.text for link in links]
        # print(f"Text of links in the sections 1, 2 is:", *links_text, sep='\n\n')
        return links_text

    # Checking links in the sections
    @allure.step("Get the list of links in sections 1, 2 on the page")
    def get_list_of_links_in_sections(self):
        links = self.elements_are_present(self.locators.SECTION_2_LINKS)
        # print(f"\nAmount of links in sections 1, 2 is: {len(links)}")
        return links

    @allure.step("Check if links are visible on the page")
    def check_visibility_of_links_in_sections(self):
        return all(link.is_displayed() for link in self.get_list_of_links_in_sections())

    @allure.step("Check if links are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links_in_sections())

    @allure.step("Get attribute 'href' of links on the page")
    def get_links_href(self):
        links = self.elements_are_present(self.locators.SECTION_2_LINKS)
        links_href = [element.get_attribute("href") for element in links]
        return links_href

    @allure.step("Check the prefix in the attribute 'href' of the email link")
    def check_email_link_href(self):
        link_href = self.get_link_href(self.locators.SECTION_2_LINK_EMAIL)
        return link_href.startswith('mailto')

    @allure.step("Get status code of links on the page")
    def get_links_status_codes(self):
        links = self.elements_are_present(self.locators.SECTION_2_LINKS_TM)
        links_href = [element.get_attribute("href") for element in links]
        links_status_codes = [requests.head(link_href).status_code for link_href in links_href]
        return links_status_codes

    @allure.step("Click on links on Telegram and thereby open corresponding web pages in new tabs")
    def click_on_links(self):
        new_tabs = []
        self.element_is_present_and_clickable(self.locators.SECTION_2_LINKS_TM_2).click()
        self.element_is_present_and_clickable(self.locators.SECTION_2_LINKS_TM_1).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_tabs.append(self.driver.current_url)
        self.driver.switch_to.window(self.driver.window_handles[2])
        new_tabs.append(self.driver.current_url)
        return new_tabs
