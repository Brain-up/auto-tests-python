"""Methods for verifying web elements on the 'Used Resources' page"""
import allure
import requests
from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.used_resources_page_locators import UsedResourcesPageLocators


class UsedResourcesPage(BasePage):
    locators = UsedResourcesPageLocators

    @allure.step("Open the 'Used resources' page")
    def open_used_resources_page(self):
        self.driver.get(MainPageLinks.URL_USED_RESOURCES_PAGE)

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 1st level of nesting on the page is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 1st level of nesting on the page are: {tags}")
        return tags

    @allure.step("Check if elements of the 1st level of nesting are visible on the page")
    def check_elements_visibility_on_1st_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)
        return all(element.is_displayed() for element in elements)

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 2nd level of nesting on the page is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 2nd level of nesting on the page are: {tags}")
        return tags

    @allure.step("Check if elements of the 2nd level of nesting are visible on the page")
    def check_elements_visibility_on_2nd_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)
        return all(element.is_displayed() for element in elements)

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 3rd level of nesting on the page is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 3rd level of nesting on the page are: {tags}")
        return tags

    @allure.step("Check if elements of the 3rd level of nesting are visible on the page")
    def check_elements_visibility_on_3rd_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)
        return all(element.is_displayed() for element in elements)

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)
        print(f"Amount of elements on the 4th level of nesting on the page is: {len(elements)}")
        tags = [element.tag_name for element in elements]
        print(f"Tags of elements on the 4th level of nesting on the page are: {tags}")
        return tags

    @allure.step("Check if elements of the 4th level of nesting are visible on the page")
    def check_elements_visibility_on_4th_level_on_page(self):
        elements = self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)
        return all(element.is_displayed() for element in elements)

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title with tag 'h1' on the page")
    def get_value_of_title_h1(self):
        return self.get_text(self.locators.TITLE_H1)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Get the list of text content in the links on the page")
    def get_text_in_links(self):
        links = self.elements_are_present(self.locators.SECTION_LINKS)
        links_text = [link.text for link in links]
        # print(f"Text in the links is:", *links_text, sep='\n\n')
        return links_text

    # Checking links in the sections
    @allure.step("Get the list of links in the sections on the page")
    def get_list_of_links(self):
        links = self.elements_are_present(self.locators.SECTION_LINKS)
        # print(f"\nAmount of links is: {len(links)}")
        return links

    @allure.step("Check all links in the sections are visible")
    def check_links_visibility(self):
        return all(link.is_displayed() for link in self.get_list_of_links())

    @allure.step("Check all links in the sections are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links in the sections")
    def get_links_href(self):
        links_href = [link.get_attribute("href") for link in self.get_list_of_links()]
        print(f"Links href in the sections are:", *links_href, sep='\n')
        return links_href

    @allure.step("Get status code of links in the sections")
    def get_links_status_codes(self):
        links_status_codes = [requests.head(link_href).status_code for link_href in self.get_links_href()]
        # print(f"Links status codes in the sections are:", *links_status_codes, sep='\n')
        return links_status_codes

    @allure.step("Click on links in the sections and thereby open corresponding web pages on new tabs")
    def click_on_links(self):
        new_tabs = [link.click() for link in self.get_list_of_links()]
        new_tabs_urls = []
        for i in range(1, len(new_tabs) + 1):
            self.driver.switch_to.window(self.driver.window_handles[i])
            new_tabs_urls.append(self.get_current_tab_url())
        print(f"New tabs url are:", *new_tabs_urls, sep='\n')
        return new_tabs_urls

    # Checking icons in the sections with links
    @allure.step("Get the list of icons in the sections")
    def get_list_of_icons(self):
        icons = self.elements_are_present(self.locators.SECTION_ICONS)
        # print(f"\nAmount of icons is: {len(icons)}")
        return icons

    @allure.step("Check all icons in the sections are visible")
    def check_icons_visibility(self):
        return all(icon.is_displayed() for icon in self.get_list_of_icons())

    @allure.step("Get attribute 'xmlns' of the icons in sections")
    def get_icons_xmlns_in_sections(self):
        return [icon.get_attribute("xmlns") for icon in self.get_list_of_icons()]

    @allure.step("Get the list of attribute 'src' values of images in specialist cards on the page")
    def get_icons_sizes(self):
        icons_sizes = [icon.size for icon in self.get_list_of_icons()]
        # print(f"The sizes of icons in sections are:", *icons_sizes, sep='\n')
        return icons_sizes

    @allure.step("""Check changes of icons sizes after resizing""")
    def check_size_changes_of_icons(self):
        icons = self.get_list_of_icons()
        icons_sizes_before = [icon.size for icon in icons]
        self.driver.set_window_size(1200, 800)
        icons_sizes_after = [icon.size for icon in icons]
        changed, lost, unchanged = 0, 0, 0
        for i in range(len(icons_sizes_after)):
            if icons_sizes_before[i] != icons_sizes_after[i]:
                changed += 1
                if icons_sizes_after[i] == {'height': 0, 'width': 0}:
                    lost += 1
            else:
                unchanged += 1
        return changed, lost, unchanged
