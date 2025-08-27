"""Methods for verifying web elements on the 'Used Resources' page"""
import allure
import requests
from pages.base_page import BasePage
from locators.used_resources_page_locators import UsedResourcesPageLocators


class UsedResourcesPage(BasePage):
    locators = UsedResourcesPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        return self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        return self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        return self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title on the page")
    def get_value_of_page_title(self):
        return self.get_text(self.locators.TITLE_H1)

    @allure.step("Get content of text on the page")
    def get_text_content_on_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Get the list of text content in links on the page")
    def get_text_in_links(self):
        return [link.text for link in self.get_list_of_links()]

    # Checking links in the sections
    @allure.step("Get the list of links in sections on the page")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.SECTION_LINKS)

    @allure.step("Check all links in sections are visible")
    def check_links_visibility(self):
        return all(link.is_displayed() for link in self.get_list_of_links())

    @allure.step("Check all links in sections are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'href' of links in sections")
    def get_links_href(self):
        return [link.get_attribute('href') for link in self.get_list_of_links()]

    @allure.step("Get status code of links in sections")
    def get_links_status_codes_brief(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href()]

    @allure.step("Get status code of links in sections")
    def get_links_status_codes(self):
        status_codes = []
        links_href = self.get_links_href()

        for link_href in links_href:
            link_status_code = requests.head(link_href).status_code
            print(f'For the link: {link_href}, \nstatus code: {link_status_code}')
            status_codes.append(link_status_code)
        return status_codes

    @allure.step("Click on links in sections and thereby open corresponding web pages on new tabs")
    def click_on_links(self):
        new_tabs = [link.click() for link in self.get_list_of_links()]
        new_tabs_urls = []
        for i in range(1, len(new_tabs) + 1):
            self.driver.switch_to.window(self.driver.window_handles[i])
            new_tabs_urls.append(self.get_current_tab_url())
        return new_tabs_urls

    # Checking icons in the sections with links
    @allure.step("Get the list of icons in sections")
    def get_list_of_icons(self):
        return self.elements_are_present(self.locators.SECTION_ICONS)

    @allure.step("Check all icons in sections are visible")
    def check_icons_visibility(self):
        return all(icon.is_displayed() for icon in self.get_list_of_icons())

    @allure.step("Get attribute 'xmlns' of icons in sections")
    def get_icons_xmlns(self):
        return [icon.get_attribute('xmlns') for icon in self.get_list_of_icons()]

    @allure.step("Get the list of sizes of icons")
    def get_icons_sizes(self):
        return [icon.size for icon in self.get_list_of_icons()]

    @allure.step("Check changes of icons sizes after resizing")
    def check_size_changes_of_icons(self):
        icons = self.get_list_of_icons()
        icons_sizes_before = [icon.size for icon in icons]
        self.driver.set_window_size(200, 700)
        icons_sizes_after = [icon.size for icon in icons]
        changed, lost, unchanged = [], [], []
        for i in range(len(icons)):
            changed.append(i) if icons_sizes_before[i] != icons_sizes_after[i] else unchanged.append(i)
            lost.append(i) if icons_sizes_after[i] == {'height': 0, 'width': 0} else None
        return changed, lost, unchanged
