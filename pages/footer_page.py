import allure
import time
from locators.footer_page_locators import FooterLocators, RelatedPagesElementsLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    locators = FooterLocators
    locators1 = RelatedPagesElementsLocators

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

    @allure.step("Check Footer is present in the DOM tree on the page")
    def check_footer_presence(self):
        return self.element_is_present(self.locators.FOOTER_SECTION)

    @allure.step("Check Footer is invisible")
    def check_footer_invisibility(self):
        return self.element_is_not_visible(self.locators.FOOTER_SECTION)

    @allure.step("Check the ARASAAC link is present in Footer")
    def check_arasaac_link_presence(self):
        return self.element_is_present(self.locators.ARASAAC_LINK)

    @allure.step("Check the ARASAAC link is visible in Footer")
    def check_arasaac_link_visibility(self):
        return self.element_is_visible(self.locators.ARASAAC_LINK)

    @allure.step("Check the ARASAAC link is clickable in Footer")
    def check_arasaac_link_clickability(self):
        return self.element_is_clickable(self.locators.ARASAAC_LINK)

    @allure.step("Click on the ARASAAC link in Footer and thereby open the corresponding web page in a new tab")
    def click_arasaac_link(self):
        self.element_is_present_and_clickable(self.locators.ARASAAC_LINK).click()

    @allure.step("Get text of the element on the ARASAAC page")
    def get_element_text_on_opened_arasaac_tab(self):
        return self.get_text(self.locators1.ARASAAC_OWNER_TITLE)

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

    @allure.step("Check the EPAM link is present in Footer")
    def check_epam_link_presence(self):
        return self.element_is_present(self.locators.EPAM_LINK)

    @allure.step("Check the EPAM link is visible in Footer")
    def check_epam_link_visibility(self):
        return self.element_is_visible(self.locators.EPAM_LINK)

    @allure.step("Check the EPAM link is clickable in Footer")
    def check_epam_link_clickability(self):
        return self.element_is_clickable(self.locators.EPAM_LINK)

    @allure.step("Click on the EPAM link in Footer and thereby open the corresponding web page in a new tab")
    def click_epam_link(self):
        self.element_is_present_and_clickable(self.locators.EPAM_LINK).click()

    @allure.step("Get text of the element on the EPAM page")
    def get_element_text_on_opened_epam_tab(self):
        return self.get_text(self.locators1.EPAM_START_PAGE_TEXT)

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

    @allure.step("Check the Jetbrains link is present in Footer")
    def check_jetbrains_link_presence(self):
        return self.element_is_present(self.locators.JETBRAINS_LINK)

    @allure.step("Check the Jetbrains link is visible in Footer")
    def check_jetbrains_link_visibility(self):
        return self.element_is_visible(self.locators.JETBRAINS_LINK)

    @allure.step("Check the Jetbrains link is clickable in Footer")
    def check_jetbrains_link_clickability(self):
        return self.element_is_clickable(self.locators.JETBRAINS_LINK)

    @allure.step("Click on the JETBRAINS link in Footer and thereby open the corresponding web page in a new tab")
    def click_jetbrains_link(self):
        self.element_is_present_and_clickable(self.locators.JETBRAINS_LINK).click()

    @allure.step("Get text of the element on the JETBRAINS page")
    def get_element_text_on_opened_jetbrains_tab(self):
        return self.get_text(self.locators1.JETBRAINS_START_PAGE_TEXT)

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

    @allure.step("Check the REG.RU link is present and visible in Footer")
    def check_reg_link_presence_and_visibility(self):
        return self.element_is_visible(self.locators.REG_LINK)

    @allure.step("Check the REG.RU link is clickable in Footer")
    def check_reg_link_clickability(self):
        return self.element_is_clickable(self.locators.REG_LINK)

    @allure.step("Click on the REG.RU link in Footer and thereby open the corresponding web page in a new tab")
    def click_reg_link(self):
        return self.element_is_present_and_clickable(self.locators.REG_LINK).click()

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

    @allure.step("Check the Selectel link is present and visible in Footer")
    def check_selectel_link_presence_and_visibility(self):
        return self.element_is_visible(self.locators.SELECTEL_LINK)

    @allure.step("Check the Selectel link is clickable in Footer")
    def check_selectel_link_clickability(self):
        return self.element_is_clickable(self.locators.SELECTEL_LINK)

    @allure.step("Click on the Selectel link in Footer and thereby open the corresponding web page in a new tab")
    def click_selectel_link(self):
        self.element_is_present_and_clickable(self.locators.SELECTEL_LINK).click()

    @allure.step("Get text of the element on the Selectel page")
    def get_element_text_on_opened_selectel_tab(self):
        return self.get_text(self.locators1.SELECTEL_START_PAGE_TEXT)

    @allure.step("Get attribute 'href' of the Selectel link")
    def get_selectel_link_href(self):
        return self.get_link_href(self.locators.SELECTEL_LINK)

    @allure.step("Check the Selectel image is present and visible in Footer")
    def check_selectel_image_visibility(self):
        return self.element_is_visible(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'src' of the Selectel image in Footer")
    def get_selectel_image_src(self):
        return self.get_image_src(self.locators.SELECTEL_IMAGE)

    @allure.step("Get attribute 'alt' of the Selectel image in Footer")
    def get_selectel_image_alt(self):
        return self.get_image_alt(self.locators.SELECTEL_IMAGE)

    @allure.step("Check the Contact us link is present and visible in Footer")
    def check_contact_us_link_presence_and_visibility(self):
        return self.element_is_visible(self.locators.CONTACT_US_LINK)

    @allure.step("Check the Contact us link is clickable in Footer")
    def check_contact_us_link_clickability(self):
        return self.element_is_clickable(self.locators.CONTACT_US_LINK)

    @allure.step("Click on the Contact us link in Footer and thereby open an email client")
    def click_contact_us_link(self):
        self.element_is_present_and_clickable(self.locators.CONTACT_US_LINK).click()

    @allure.step("Get attribute 'href' of the Contact us link")
    def get_contact_us_link_href(self):
        return self.get_link_href(self.locators.CONTACT_US_LINK)

    @allure.step("Check the prefix and the subject in the attribute 'href' of the Contact us link")
    def check_contact_us_link_href(self):
        link_href = self.get_contact_us_link_href()
        return "mailto" in link_href, "subject=BrainUp" in link_href
