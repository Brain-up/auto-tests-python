"""Methods for verifying web elements on the starting page for unauthorized users"""
import allure
import requests
from pages.base_page import BasePage
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from locators.login_page_locators import LoginPageLocators


class StartUnauthorizedPage(BasePage):
    locators = StartUnauthorizedPageLocators
    locators1 = LoginPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections_on_page(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        return len(sections)

    @allure.step("Check sections are visible")
    def check_visibility_of_sections(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        return all(section.is_displayed() for section in sections)

    @allure.step("Get structure of the 1st level of nesting in the section 1")
    def get_structure_of_1st_level_in_section1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible in the section 1")
    def check_elements_visibility_on_1st_level_in_section1(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level_in_section1())

    @allure.step("Get structure of the 2nd level of nesting in the section 1")
    def get_structure_of_2nd_level_in_section1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible in the section 1")
    def check_elements_visibility_on_2nd_level_in_section1(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level_in_section1())

    @allure.step("Get structure of the 3rd level of nesting in the section 1")
    def get_structure_of_3rd_level_in_section1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible in the section 1")
    def check_visibility_of_elements_on_3rd_level_in_section1(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level_in_section1())

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

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get the list of titles h2 on the page")
    def get_list_of_titles(self):
        return self.elements_are_present(self.locators.PAGE_TITLES)

    @allure.step("Get the list of title values")
    def get_values_of_titles(self):
        return [title.text for title in self.get_list_of_titles()]

    @allure.step("Get the list of subtitles h4 on the page")
    def get_list_of_subtitles(self):
        return self.elements_are_present(self.locators.PAGE_SUBTITLES)

    @allure.step("Get the list of subtitle values")
    def get_values_of_subtitles(self):
        return [subtitle.text for subtitle in self.get_list_of_subtitles()]

    @allure.step("Get content of the text in the section 1")
    def get_text_content_in_section1(self):
        return self.get_text(self.locators.SECTION_1_TEXT)

    @allure.step("Get the list of elements with text in the section 2")
    def get_list_of_elements_with_text_in_section2(self):
        return self.elements_are_present(self.locators.SECTION_2_TEXT)

    @allure.step("Get the list of text content in the section 2")
    def get_text_content_in_section2(self):
        return [element.text for element in self.get_list_of_elements_with_text_in_section2()]

    @allure.step("Get text in the 'Login' link in the section 1")
    def get_text_in_login_link(self):
        return self.get_text(self.locators.SECTION_1_LINK_LOGIN)

    # Checking the 'Login' link in the section 1
    @allure.step("Check the 'Login' link is present in DOM")
    def check_login_link_presence(self):
        return self.element_is_present(self.locators.SECTION_1_LINK_LOGIN)

    @allure.step("Check the 'Login' link is visible")
    def check_login_link_visibility(self):
        return self.element_is_visible(self.locators.SECTION_1_LINK_LOGIN)

    @allure.step("Check the 'Login' link is clickable")
    def check_login_link_clickability(self):
        return self.element_is_clickable(self.locators.SECTION_1_LINK_LOGIN)

    @allure.step("Get attribute 'href' of the 'Login' link")
    def get_login_link_href(self):
        return self.get_link_href(self.locators.SECTION_1_LINK_LOGIN)

    @allure.step("Get status code of the 'Login' link")
    def get_login_link_status_code(self):
        return requests.head(self.get_login_link_href()).status_code

    @allure.step("Click on the 'Login' link and thereby open the corresponding web page in the same tab")
    def click_login_link(self):
        self.element_is_present_and_clickable(self.locators.SECTION_1_LINK_LOGIN).click()

    @allure.step("Get text of the element on the 'Login' page")
    def get_element_text_on_opened_login_page(self):
        return self.get_text(self.locators1.SIGN_IN_TAB)

# Checking the image in the section 1
    @allure.step("Check the image is present in the section 1")
    def check_image_presence(self):
        return self.element_is_present(self.locators.SECTION_1_IMAGE)

    @allure.step("Check the image is visible")
    def check_image_visibility(self):
        return self.element_is_visible(self.locators.SECTION_1_IMAGE)

    @allure.step("Get attribute 'src' of the image")
    def get_src_of_image(self):
        return self.get_image_src(self.locators.SECTION_1_IMAGE)

    @allure.step("Get attribute 'alt' of the image")
    def get_alt_of_image(self):
        return self.get_image_alt(self.locators.SECTION_1_IMAGE)

    @allure.step("Get size values of the image")
    def get_size_of_image(self):
        return self.get_image_size(self.locators.SECTION_1_IMAGE)

    @allure.step("Check changes of image size values after resizing")
    def check_size_changes_of_image(self):
        image_size_before = self.get_size_of_image()
        self.driver.set_window_size(1200, 800)
        image_size_after = self.get_size_of_image()
        print("The image sizes are changed") if image_size_before != image_size_after else print("No changes of sizes")
        print("The image sizes became zero after resizing") if image_size_before == {'height': 0, 'width': 0} else None
        return image_size_after
