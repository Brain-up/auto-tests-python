import allure
import requests
from selenium.common import TimeoutException
from locators.footer_page_locators import FooterLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    locators = FooterLocators

    # Checking the structure and display of elements in the Footer
    @allure.step("Check the Footer is present in the DOM tree on the page")
    def check_footer_presence(self):
        return self.element_is_present(self.locators.FOOTER)

    @allure.step("Check if the Footer is visible on the page")
    def check_footer_visibility(self):
        return self.element_is_visible(self.locators.FOOTER)

    @allure.step("Check the Footer is invisible")
    def check_footer_invisibility(self):
        return self.element_is_not_visible(self.locators.FOOTER)

    @allure.step("Get structure of the 1st level of nesting in the Footer")
    def get_structure_of_1st_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_FIRST_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting in the Footer")
    def get_structure_of_2nd_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_SECOND_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting in the Footer")
    def get_structure_of_3rd_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_THIRD_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting in the Footer")
    def get_structure_of_4th_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_FOURTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting in the Footer")
    def get_structure_of_5th_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_FIFTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting in the Footer")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_SIXTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Get structure of the 7th level of nesting in the Footer")
    def get_structure_of_7th_level(self):
        elements = self.elements_are_present(self.locators.FOOTER_SEVENTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 7th level of nesting are visible")
    def check_elements_visibility_on_7th_level_on_page(self):
        return all(element.is_displayed() for element in self.get_structure_of_7th_level())

    @allure.step("Check text on the 4th level of nesting is present in the Footer")
    def check_text_presence(self):
        return self.element_is_present(self.locators.FOOTER_TEXT)

    @allure.step("Check text in the Footer is visible")
    def check_text_visibility(self):
        return self.element_is_visible(self.locators.FOOTER_TEXT)

    @allure.step("Get the list of links on the 6th level of nesting in the Footer")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.FOOTER_LINKS)

    @allure.step("Get the list of links to supporters")
    def get_list_of_supporter_links(self):
        return self.elements_are_present(self.locators.SUPPORTER_LINKS)

    @allure.step("Check links in the Footer are visible")
    def check_links_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_links())

    @allure.step("Get the list of images on the 7th level of nesting in the Footer")
    def get_list_of_images(self):
        return self.elements_are_present(self.locators.FOOTER_IMAGES)

    @allure.step("Check images in the Footer are visible")
    def check_images_visibility(self):
        return all(element.is_displayed() for element in self.get_list_of_images())

    @allure.step("Check the Jetbrains image is present in the DOM tree")
    def check_jetbrains_image_presence(self):
        return self.element_is_present(self.locators.JETBRAINS_IMAGE)

    @allure.step("Check the Jetbrains image is invisible in the Footer")
    def check_jetbrains_image_invisibility(self):
        return self.element_is_not_visible(self.locators.JETBRAINS_IMAGE)

    # Checking text in the Footer
    @allure.step("Get content of text in the Footer")
    def get_footer_text(self):
        return self.get_text(self.locators.WITH_THE_SUPPORT_TEXT)

    @allure.step("Get text in the 'Contact us' link in the Footer")
    def get_text_in_contact_us_link(self):
        return self.get_text(self.locators.CONTACT_US_LINK)

    # Checking links in the Footer
    @allure.step("Check if links are clickable in the Footer")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'title' of the 'Contact us' link")
    def get_contact_us_link_title(self):
        return self.get_link_title(self.locators.CONTACT_US_LINK)

    @allure.step("Get attribute 'href' of links in the Footer")
    def get_links_href(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Get attribute 'href' of the 'Contact us' link")
    def get_contact_us_link_href(self):
        return self.get_link_href(self.locators.CONTACT_US_LINK)

    @allure.step("Check the prefix and the subject in the attribute 'href' of the 'Contact us' link")
    def check_contact_us_link_href(self):
        link_href = self.get_contact_us_link_href()
        return link_href.startswith('mailto'), link_href.endswith('subject=BrainUp')

    @allure.step("Get status code of links to supporters")
    def get_supporter_links_status_codes(self):
        links_href = [element.get_attribute("href") for element in self.get_list_of_supporter_links()]
        return [requests.head(link_href).status_code for link_href in links_href]

    @allure.step("Click on links in the Footer and thereby open corresponding web pages on new tabs")
    def click_on_links(self):
        new_tabs = [link.click() for link in self.get_list_of_supporter_links()]
        # print(f'Opened tabs: {len(new_tabs)}')
        new_tabs_urls, count1, count2, count3 = [], 0, 0, 0
        for i in range(1, len(new_tabs) + 1):
            try:
                self.driver.switch_to.window(self.driver.window_handles[i])
                new_tab_url = self.get_current_tab_url()
                if new_tab_url:
                    new_tabs_urls.append(new_tab_url)
                    count1 += 1
                else:
                    print(f"The tab url {i} has not been defined during the allotted time")
                    count2 += 1
            except TimeoutException:
                print(f"The tab {i} has not been loaded during the allotted time")
                count3 += 1
        # print(f'{new_tabs_urls}\nDefined tabs urls: {count1}\nUndefined tabs urls: {count2}\nUnloaded tabs: {count3}')
        return new_tabs_urls

    @allure.step("Click on the 'Contact us' link in the Footer and thereby open an email client")
    def click_contact_us_link(self):
        self.element_is_present_and_clickable(self.locators.CONTACT_US_LINK).click()

    # Checking images in the Footer
    @allure.step("Get the list of attribute 'src' values of images in links")
    def get_images_src(self):
        return [image.get_attribute('src') for image in self.get_list_of_images()]

    @allure.step("Get the list of attribute 'alt' values of images in links")
    def get_images_alt(self):
        return [image.get_attribute('alt') for image in self.get_list_of_images()]

    @allure.step("Get the list of sizes of images in links")
    def get_images_sizes(self):
        return [image.size for image in self.get_list_of_images()]

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images(self):
        images = self.get_list_of_images()
        images_sizes_before = [image.size for image in images]
        self.driver.set_window_size(400, 700)
        images_sizes_after = [image.size for image in images]
        changed, lost, unchanged = [], [], []
        for i in range(len(images)):
            changed.append(i) if images_sizes_before[i] != images_sizes_after[i] else unchanged.append(i)
            lost.append(i) if images_sizes_after[i] == {'height': 0, 'width': 0} else None
        # print('All images have changed sizes' if len(changed) == len(images) else 'Not all images have changed sizes')
        return changed
