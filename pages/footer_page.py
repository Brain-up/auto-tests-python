import time
import allure
import requests
from locators.footer_page_locators import FooterLocators, RelatedPagesElementsLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    locators = FooterLocators
    locators1 = RelatedPagesElementsLocators

    # Checking the structure and display of elements in the Footer
    @allure.step("Check Footer is present in the DOM tree on the page")
    def check_footer_presence(self):
        return self.element_is_present(self.locators.FOOTER)

    @allure.step("Check if Footer is visible on the page")
    def check_footer_visibility(self):
        return self.element_is_visible(self.locators.FOOTER)

    @allure.step("Check Footer is invisible")
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

    @allure.step("Get attribute 'href' of in the Footer")
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
        new_tabs_urls = []
        for i in range(1, len(new_tabs) + 1):
            self.driver.switch_to.window(self.driver.window_handles[i])
            time.sleep(5)
            new_tabs_urls.append(self.get_current_tab_url())
        return new_tabs_urls

    @allure.step("Click on the 'Contact us' link in the Footer and thereby open an email client")
    def click_contact_us_link(self):
        self.element_is_present_and_clickable(self.locators.CONTACT_US_LINK).click()

    @allure.step("Find the element on the page")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Get attribute 'src' of an element's image")
    def get_image_src(self, locator):
        return self.driver.find_element(*locator).get_attribute("src")

    @allure.step("Get attribute 'alt' of an element's image")
    def get_image_alt(self, locator):
        return self.driver.find_element(*locator).get_attribute("alt")

    @allure.step("Get attribute 'width' of an element's image")
    def get_image_width(self, locator):
        return self.driver.find_element(*locator).get_attribute("width")

    @allure.step("Get attribute 'height' of an element's image")
    def get_image_height(self, locator):
        return self.driver.find_element(*locator).get_attribute("height")

    @allure.step("Get attribute 'href' of the ARASAAC link")
    def get_arasaac_link_href(self):
        return self.get_link_href(self.locators.ARASAAC_LINK)

    @allure.step("Check the ARASAAC image is present in Footer")
    def check_arasaac_image_presence(self):
        return self.element_is_present(self.locators.ARASAAC_IMAGE)

    @allure.step("Check the ARASAAC image is visible in Footer")
    def check_arasaac_image_visibility(self):
        return self.element_is_visible(self.locators.ARASAAC_IMAGE)

    @allure.step("Get attribute 'src' of the ARASAAC image in Footer")
    def get_arasaac_image_src(self):
        return self.get_image_src(self.locators.ARASAAC_IMAGE)

    @allure.step("Get attribute 'alt' of the ARASAAC image in Footer")
    def get_arasaac_image_alt(self):
        return self.get_image_alt(self.locators.ARASAAC_IMAGE)

    @allure.step("Get attribute 'width' of the ARASAAC image in Footer")
    def get_visible_width_of_arasaac_image(self):
        return self.get_image_width(self.locators.ARASAAC_IMAGE)

    @allure.step("Get attribute 'height' of the ARASAAC image in Footer")
    def get_visible_height_of_arasaac_image(self):
        return self.get_image_height(self.locators.ARASAAC_IMAGE)

    @allure.step("Get attribute 'href' of the EPAM link")
    def get_epam_link_href(self):
        return self.get_link_href(self.locators.EPAM_LINK)

    @allure.step("Check the EPAM image is present in Footer")
    def check_epam_image_presence(self):
        return self.element_is_present(self.locators.EPAM_IMAGE)

    @allure.step("Check the EPAM image is present and visible in Footer")
    def check_epam_image_visibility(self):
        return self.element_is_visible(self.locators.EPAM_IMAGE)

    @allure.step("Get attribute 'src' of the EPAM image in Footer")
    def get_epam_image_src(self):
        return self.get_image_src(self.locators.EPAM_IMAGE)

    @allure.step("Get attribute 'alt' of the EPAM image in Footer")
    def get_epam_image_alt(self):
        return self.get_image_alt(self.locators.EPAM_IMAGE)

    @allure.step("Get attribute 'width' of the EPAM image in Footer")
    def get_visible_width_of_epam_image(self):
        return self.get_image_width(self.locators.EPAM_IMAGE)

    @allure.step("Get attribute 'height' of the EPAM image in Footer")
    def get_visible_height_of_epam_image(self):
        return self.get_image_height(self.locators.EPAM_IMAGE)

    @allure.step("Get attribute 'href' of the Jetbrains link")
    def get_jetbrains_link_href(self):
        return self.get_link_href(self.locators.JETBRAINS_LINK)

    @allure.step("Check the Jetbrains image is present in the DOM tree on the page")
    def check_jetbrains_image_presence(self):
        return self.element_is_present(self.locators.JETBRAINS_IMAGE)

    @allure.step("Check the Jetbrains image is present and visible in Footer")
    def check_jetbrains_image_visibility(self):
        return self.element_is_visible(self.locators.JETBRAINS_IMAGE)

    @allure.step("Check the Jetbrains image is invisible in Footer")
    def check_jetbrains_image_invisibility(self):
        return self.element_is_not_visible(self.locators.JETBRAINS_IMAGE)

    @allure.step("Get attribute 'src' of the Jetbrains image in Footer")
    def get_jetbrains_image_src(self):
        return self.get_image_src(self.locators.JETBRAINS_IMAGE)

    @allure.step("Get attribute 'alt' of the Jetbrains image in Footer")
    def get_jetbrains_image_alt(self):
        return self.get_image_alt(self.locators.JETBRAINS_IMAGE)

    @allure.step("Get attribute 'width' of the Jetbrains image in Footer")
    def get_visible_width_of_jetbrains_image(self):
        return self.get_image_width(self.locators.JETBRAINS_IMAGE)

    @allure.step("Get attribute 'height' of the Jetbrains image in Footer")
    def get_visible_height_of_jetbrains_image(self):
        return self.get_image_height(self.locators.JETBRAINS_IMAGE)

    @allure.step("Get attribute 'href' of the REG.RU link")
    def get_reg_link_href(self):
        return self.get_link_href(self.locators.REG_LINK)

    @allure.step("Check the REG.RU image is present in Footer")
    def check_reg_image_presence(self):
        return self.element_is_present(self.locators.REG_IMAGE)

    @allure.step("Check the REG.RU image is visible in Footer")
    def check_reg_image_visibility(self):
        return self.element_is_visible(self.locators.REG_IMAGE)

    @allure.step("Get attribute 'src' of the REG.RU image in Footer")
    def get_reg_image_src(self):
        return self.get_image_src(self.locators.REG_IMAGE)

    @allure.step("Get attribute 'alt' of the REG.RU image in Footer")
    def get_reg_image_alt(self):
        return self.get_image_alt(self.locators.REG_IMAGE)

    @allure.step("Get attribute 'width' of the REG.RU image in Footer")
    def get_visible_width_of_reg_image(self):
        return self.get_image_width(self.locators.REG_IMAGE)

    @allure.step("Get attribute 'height' of the REG.RU image in Footer")
    def get_visible_height_of_reg_image(self):
        return self.get_image_height(self.locators.REG_IMAGE)

    @allure.step("Get attribute 'href' of the Selectel link")
    def get_selectel_link_href(self):
        return self.get_link_href(self.locators.SELECTEL_LINK)

    @allure.step("Check the Selectel image is present in Footer")
    def check_selectel_image_presence(self):
        return self.element_is_present(self.locators.SELECTEL_IMAGE)

    @allure.step("Check the Selectel image is visible in Footer")
    def check_selectel_image_visibility(self):
        return self.element_is_visible(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'src' of the Selectel image in Footer")
    def get_selectel_image_src(self):
        return self.get_image_src(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'alt' of the Selectel image in Footer")
    def get_selectel_image_alt(self):
        return self.get_image_alt(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'width' of the Selectel image in Footer")
    def get_visible_width_of_selectel_image(self):
        return self.get_image_width(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'height' of the Selectel image in Footer")
    def get_visible_height_of_selectel_image(self):
        return self.get_image_height(self.locators.SELECTEL_IMAGE)
