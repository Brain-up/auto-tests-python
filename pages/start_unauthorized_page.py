"""Methods for verifying web elements on the starting page for unauthorized users"""
import allure
from pages.base_page import BasePage
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators
from locators.login_page_locators import LoginPageLocators


class StartUnauthorizedPage(BasePage):
    locators = StartUnauthorizedPageLocators
    locators1 = LoginPageLocators

    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections_on_page(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        # print(len(sections))
        return len(sections)

    @allure.step("Check sections are visible on the page")
    def check_visibility_of_sections(self):
        sections = self.elements_are_present(self.locators.PAGE_SECTIONS)
        for section in sections:
            return section.is_displayed()

    @allure.step("Get structure of section 1 with content on the page")
    def get_structure_of_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 1st level of nesting in the section 1 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 1st level of nesting in the section 1 are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level are visible in the section 1")
    def check_visibility_of_elements_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_FIRST_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of subsections in section 1 with content on the page")
    def get_structure_of_subsection_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_SECOND_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 2nd level of nesting in the section 1 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 2nd level of nesting in the section 1 are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible in the section 1")
    def check_visibility_of_elements_in_subsection_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_SECOND_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-subsections in section 1 with content on the page")
    def get_structure_of_3th_level_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_THIRD_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 3rd level of nesting in the section 1 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 3rd level of nesting in the section 1 are: {tags}")
        return tags

    @allure.step("Check if elements of the 3rd level of nesting are visible in the section 1")
    def check_visibility_of_elements_on_3th_level_in_section_1(self):
        elements = self.elements_are_present(self.locators.SECTION_1_THIRD_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of section 2 with content on the page")
    def get_structure_of_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIRST_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 1st level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 1st level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level are visible in the section 2")
    def check_visibility_of_elements_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_FIRST_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of subsections in section 2 with content on the page")
    def get_structure_of_subsection_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_SECOND_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 2nd level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 2nd level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible in the section 2")
    def check_visibility_of_elements_in_subsection_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_SECOND_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get structure of sub-subsections in section 2 with content on the page")
    def get_structure_of_3rd_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_THIRD_LEVEL_ELEMENTS)
        # print(f"Amount of elements on the 3rd level of nesting in the section 2 is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        # print(f"Tags of elements on the 3rd level of nesting in the section 2 are: {tags}")
        return tags

    @allure.step("Check if elements of the 3rd level of nesting are visible in the section 2")
    def check_visibility_of_elements_on_3rd_level_in_section_2(self):
        elements = self.elements_are_present(self.locators.SECTION_2_THIRD_LEVEL_ELEMENTS)
        for element in elements:
            return element.is_displayed()

    @allure.step("Get the list of titles on the page")
    def get_list_of_titles_on_page(self):
        titles = self.elements_are_present(self.locators.PAGE_TITLES)
        # print(f"\nAmount of titles on the page is: {len(titles)}")
        return titles

    @allure.step("Get the list of title values on the page")
    def get_values_of_titles(self):
        titles = self.get_list_of_titles_on_page()
        title_values = [title.text for title in titles]
        # print(f"The title values on the page are:", *title_values, sep='\n')
        return title_values

    @allure.step("Get the list of subtitles on the page")
    def get_list_of_subtitles_on_page(self):
        subtitles = self.elements_are_present(self.locators.PAGE_SUBTITLES)
        # print(f"\nAmount of subtitles on the page is: {len(subtitles)}")
        return subtitles

    @allure.step("Get the list of subtitle values on the page")
    def get_values_of_subtitles(self):
        subtitles = self.get_list_of_subtitles_on_page()
        subtitle_values = [subtitle.text for subtitle in subtitles]
        # print(f"The subtitle values on the page are:", *subtitle_values, sep='\n')
        return subtitle_values

    @allure.step("Get content of the text in the section 1 on the page")
    def get_values_of_text_in_section_1(self):
        return self.get_text(self.locators.SECTION_1_TEXT)

    @allure.step("Get the list of elements with text in the section 2 on the page")
    def get_list_of_elements_with_text_in_section_2(self):
        elements_with_text = self.elements_are_present(self.locators.SECTION_2_TEXT)
        # print(f"\nAmount of elements with text in the section 2 is: {len(elements_with_text)}")
        return elements_with_text

    @allure.step("Get the list of text content in the section 2 on the page")
    def get_values_of_text_in_section_2(self):
        elements_with_text = self.get_list_of_elements_with_text_in_section_2()
        element_values = [element.text for element in elements_with_text]
        # print(f"The content of the text in the section 2 are:", *element_values, sep='\n\n')
        return element_values

    @allure.step("Get attribute 'src' of the image in the section 1 on the page")
    def get_image_src_in_section_1(self):
        return self.get_image_src(self.locators.SECTION_1_IMAGE)

    @allure.step("Get attribute 'alt' of the image in the section 1 on the page")
    def get_image_alt_in_section_1(self):
        return self.get_image_alt(self.locators.SECTION_1_IMAGE)

    @allure.step("Get size values of the image in the section 1 on the page")
    def get_visible_size_of_image_in_section_1(self):
        return self.get_image_size(self.locators.SECTION_1_IMAGE)

    @allure.step("Get size values of image in the section 1 on the page and check its changes after resizing")
    def check_size_changes_of_image_in_section_1(self):
        image_size_before = self.get_visible_size_of_image_in_section_1()
        # print(f"The visible sizes of the image in section 1 are: {image_size_before}")
        self.driver.set_window_size(1200, 800)
        image_size_after = self.get_visible_size_of_image_in_section_1()
        # print(f"The visible sizes of the image in section 1 are: {image_size_after}")
        if image_size_before != image_size_after:
            # print(f"\n   The image in the section 1 has sizes that changed: \nfrom {image_size_before} before "
            #       f"resizing \nto {image_size_after} after resizing")
            return image_size_before, image_size_after

    @allure.step("Check the 'Login' link is present in DOM")
    def check_login_link_presence(self):
        return self.element_is_present(self.locators.SECTION_1_LINK)

    @allure.step("Check the 'Login' link is visible on the page")
    def check_login_link_visibility(self):
        return self.element_is_visible(self.locators.SECTION_1_LINK)

    @allure.step("Check the 'Login' link is clickable")
    def check_login_link_clickability(self):
        return self.element_is_clickable(self.locators.SECTION_1_LINK)

    @allure.step("Get attribute 'href' of the 'Login' link")
    def get_login_link_href(self):
        return self.get_link_href(self.locators.SECTION_1_LINK)

    @allure.step("Get text in the 'Login' link")
    def get_text_in_login_link(self):
        return self.get_text(self.locators.SECTION_1_LINK)

    @allure.step("Click on the 'Login' link and thereby open the corresponding web page in the same tab")
    def click_login_link(self):
        self.element_is_present_and_clickable(self.locators.SECTION_1_LINK).click()
        print(self.driver.current_url)

    @allure.step("Get text of the element on the 'Login' page")
    def get_element_text_on_opened_login_page(self):
        text_on_opened_page = self.get_text(self.locators1.SIGN_IN_TAB)
        print(text_on_opened_page)
        return text_on_opened_page
