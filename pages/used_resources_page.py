"""Methods for verifying web elements on the 'Used Resources' page"""
import allure
import requests
from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.used_resources_page_locators import UsedResourcesPageLocators, RelatedPagesElementsLocators


class UsedResourcesPage(BasePage):
    locators = UsedResourcesPageLocators
    locators1 = RelatedPagesElementsLocators

    @allure.step("Open the 'Used resources' page")
    def open_used_resources_page(self):
        self.driver.get(MainPageLinks.URL_USED_RESOURCES_PAGE)

    @allure.step("Check the page title is present in DOM")
    def check_used_resources_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the page title is visible on the page")
    def check_used_resources_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get content of the title on the page")
    def get_used_resources_page_title_content(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    @allure.step("Check the page text is present in DOM")
    def check_used_resources_page_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the page text is visible on the page")
    def check_used_resources_page_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_the_used_resources_page(self):
        return self.element_is_visible(self.locators.PAGE_TEXT).text

    @allure.step("Check if the section with links is present in DOM")
    def check_presence_of_links_section_on_used_resources_page(self):
        return self.element_is_present(self.locators.LINKS_SECTION)

    @allure.step("Check if the section with links is visible on the page")
    def check_visibility_of_links_section_on_used_resources_page(self):
        return self.element_is_visible(self.locators.LINKS_SECTION)

    @allure.step("Check if the section with the freepik.com link is present in DOM")
    def check_presence_of_freepik_com_link_section(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK_SECTION)

    @allure.step("Check if the section with the freepik.com link is visible on the page")
    def check_visibility_of_freepik_com_link_section(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_LINK_SECTION)

    @allure.step("Click on the freepik.com link and thereby open the corresponding web page in a new tab")
    def click_freepik_com_link(self):
        self.element_is_present_and_clickable(self.locators.FREEPIK_COM_LINK).click()

    @allure.step("Get text of the element on the freepik.com page")
    def get_element_text_on_opened_freepik_com_tab(self):
        return self.get_text(self.locators1.FREEPIK_COM_TEXT)

    @allure.step("Get content of the text in the freepik.com link")
    def get_text_in_freepik_com_link(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK).text

    @allure.step("Check if the section with the 'Plants' link is present in DOM")
    def check_presence_of_plants_link_section(self):
        return self.element_is_present(self.locators.PLANTS_LINK_SECTION)

    @allure.step("Check if the section with the 'Plants' link is visible on the page")
    def check_visibility_of_plants_link_section(self):
        return self.element_is_visible(self.locators.PLANTS_LINK_SECTION)

    @allure.step("Click on the 'Plants' link and thereby open the corresponding web page in a new tab")
    def click_plants_link(self):
        self.element_is_present_and_clickable(self.locators.PLANTS_LINK).click()

    @allure.step("Get text of the element on the 'Plants' page")
    def get_element_text_on_opened_plants_tab(self):
        return self.get_text(self.locators1.PLANTS_TEXT)

    @allure.step("Get content of the text in the 'Plants' link")
    def get_text_in_plants_link(self):
        return self.element_is_present(self.locators.PLANTS_LINK).text

    @allure.step("Check if the section with the 'Flora' link is present in DOM")
    def check_presence_of_flora_link_section(self):
        return self.element_is_present(self.locators.FLORA_LINK_SECTION)

    @allure.step("Check if the section with the 'Flora' link is visible on the page")
    def check_visibility_of_flora_link_section(self):
        return self.element_is_visible(self.locators.FLORA_LINK_SECTION)

    @allure.step("Click on the 'Flora' link and thereby open the corresponding web page in a new tab")
    def click_flora_link(self):
        self.element_is_present_and_clickable(self.locators.FLORA_LINK).click()

    @allure.step("Get text of the element on the 'Flora' page")
    def get_element_text_on_opened_flora_tab(self):
        return self.get_text(self.locators1.FLORA_TEXT)

    @allure.step("Get content of the text in the 'Flora' link")
    def get_text_in_flora_link(self):
        return self.element_is_present(self.locators.FLORA_LINK).text

    # Checks of links in the sections
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
        # print(f"Links href in the sections are:", *links_href, sep='\n')
        return links_href

    @allure.step("Get status code of links in the sections")
    def get_links_status_codes(self):
        links_status_codes = [requests.head(link_href).status_code for link_href in self.get_links_href()]
        # print(f"Links status codes in the sections are:", *links_status_codes, sep='\n')
        return links_status_codes

    # Checks of icons in the sections with links
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
        # print("The results of checking changes of icon sizes after resizing are:")
        changed, lost, unchanged = 0, 0, 0
        for i in range(len(icons_sizes_after)):
            if icons_sizes_before[i] != icons_sizes_after[i]:
                changed += 1
                if icons_sizes_after[i] == {'height': 0, 'width': 0}:
                    lost += 1
                    # print(f"\n   The icon #{i + 1} has become invisible because has sizes that changed: "
                    #       f"\nfrom {icons_sizes_before[i]} before resizing \n"
                    #       f"to {icons_sizes_after[i]} after resizing")
                # else:
                    # print(f"\n   The icon #{i + 1} has sizes that changed: \nfrom {icons_sizes_before[i]} before "
                    #       f"resizing \nto {icons_sizes_after[i]} after resizing")
            else:
                unchanged += 1
                # print(
                #     f"\n   The icon #{i + 1} has sizes that remain: "
                #     f"\nthe same {icons_sizes_before[i]} before resizing "
                #     f"\nand {icons_sizes_after[i]} after resizing")
        # print(f"\nSummary of icon size checks\n   Amount of icons with changed sizes after resizing is: {changed}, "
        #       f"\nincluding icons that have become invisible on the page: {lost}")
        # print(f"   Amount of icons with unchanged sizes after resizing is: {unchanged}")
        return changed, lost, unchanged
