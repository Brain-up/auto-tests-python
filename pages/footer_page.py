import allure
from locators.footer_page_locators import FooterLocators, RelatedPagesElementsLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    @allure.step('Find the element on the page')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Get attribute 'src' of an element's image")
    def get_image_src(self, locator):
        return self.driver.find_element(*locator).get_attribute("src")

    @allure.step("Get attribute 'alt' of an element's image")
    def get_image_alt(self, locator):
        return self.driver.find_element(*locator).get_attribute("alt")

    @allure.step("Get attribute 'href' of link")
    def get_link_href(self, locator):
        return self.driver.find_element(*locator).get_attribute("href")

    @allure.step('Check Footer is present in the DOM tree on the page')
    def check_footer_presence(self):
        return self.element_is_present(FooterLocators.FOOTER_SECTION)

    @allure.step('Check Footer is invisible')
    def check_footer_invisibility(self):
        return self.element_is_not_visible(FooterLocators.FOOTER_SECTION)

    @allure.step('Check the ARASAAC link is present and visible in Footer')
    def check_arasaac_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.ARASAAC_LINK)

    @allure.step('Check the ARASAAC link is clickable in Footer')
    def check_arasaac_link_clickability(self):
        return self.element_is_clickable(FooterLocators.ARASAAC_LINK)

    @allure.step('Click on the ARASAAC link in Footer and thereby open the corresponding web page in a new tab')
    def click_arasaac_link(self):
        self.element_is_present_and_clickable(FooterLocators.ARASAAC_LINK).click()

    @allure.step("Get text of the element on the ARASAAC page")
    def get_element_text_on_opened_arasaac_tab(self):
        return self.get_text(RelatedPagesElementsLocators.ARASAAC_OWNER_TITLE)

    @allure.step("Get attribute 'href' of the ARASAAC link")
    def get_arasaac_link_href(self):
        return self.get_link_href(FooterLocators.ARASAAC_LINK)

    @allure.step('Check the ARASAAC image is present and visible in Footer')
    def check_arasaac_image_visibility(self):
        return self.element_is_visible(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Get attribute "src" of the ARASAAC image in Footer')
    def get_arasaac_image_src(self):
        return self.get_image_src(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Get attribute "alt" of the ARASAAC image in Footer')
    def get_arasaac_image_alt(self):
        return self.get_image_alt(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Check the EPAM link is present and visible in Footer')
    def check_epam_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.EPAM_LINK)

    @allure.step('Check the EPAM link is clickable in Footer')
    def check_epam_link_clickability(self):
        return self.element_is_clickable(FooterLocators.EPAM_LINK)

    @allure.step('Click on the EPAM link in Footer and thereby open the corresponding web page in a new tab')
    def click_epam_link(self):
        self.element_is_present_and_clickable(FooterLocators.EPAM_LINK).click()

    @allure.step("Get text of the element on the EPAM page")
    def get_element_text_on_opened_epam_tab(self):
        return self.get_text(RelatedPagesElementsLocators.EPAM_START_PAGE_TEXT)

    @allure.step("Get attribute 'href' of the EPAM link")
    def get_epam_link_href(self):
        return self.get_link_href(FooterLocators.EPAM_LINK)

    @allure.step('Check the EPAM image is present and visible in Footer')
    def check_epam_image_visibility(self):
        return self.element_is_visible(FooterLocators.EPAM_IMAGE)

    @allure.step('Get attribute "src" of the EPAM image in Footer')
    def get_epam_image_src(self):
        return self.get_image_src(FooterLocators.EPAM_IMAGE)

    @allure.step('Get attribute "alt" of the EPAM image in Footer')
    def get_epam_image_alt(self):
        return self.get_image_alt(FooterLocators.EPAM_IMAGE)

    @allure.step('Check the Jetbrains link is present and visible in Footer')
    def check_jetbrains_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.JETBRAINS_LINK)

    @allure.step('Check the Jetbrains link is clickable in Footer')
    def check_jetbrains_link_clickability(self):
        return self.element_is_clickable(FooterLocators.JETBRAINS_LINK)

    @allure.step('Click on the JETBRAINS link in Footer and thereby open the corresponding web page in a new tab')
    def click_jetbrains_link(self):
        self.element_is_present_and_clickable(FooterLocators.JETBRAINS_LINK).click()

    @allure.step("Get text of the element on the JETBRAINS page")
    def get_element_text_on_opened_jetbrains_tab(self):
        return self.get_text(RelatedPagesElementsLocators.JETBRAINS_START_PAGE_TEXT)

    @allure.step("Get attribute 'href' of the Jetbrains link")
    def get_jetbrains_link_href(self):
        return self.get_link_href(FooterLocators.JETBRAINS_LINK)

    @allure.step('Check the Jetbrains image is present in the DOM tree on the page')
    def check_jetbrains_image_presence(self):
        return self.element_is_present(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check the Jetbrains image is present and visible in Footer')
    def check_jetbrains_image_visibility(self):
        return self.element_is_visible(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check the Jetbrains image is invisible in Footer')
    def check_jetbrains_image_invisibility(self):
        return self.element_is_not_visible(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Get attribute "src" of the Jetbrains image in Footer')
    def get_jetbrains_image_src(self):
        return self.get_image_src(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Get attribute "alt" of the Jetbrains image in Footer')
    def get_jetbrains_image_alt(self):
        return self.get_image_alt(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check the REG.RU link is present and visible in Footer')
    def check_reg_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.REG_LINK)

    @allure.step('Check the REG.RU link is clickable in Footer')
    def check_reg_link_clickability(self):
        return self.element_is_clickable(FooterLocators.REG_LINK)

    @allure.step('Click on the REG.RU link in Footer and thereby open the corresponding web page in a new tab')
    def click_reg_link(self):
        self.element_is_present_and_clickable(FooterLocators.REG_LINK).click()

    @allure.step("Get text of the element on the REG.RU page")
    def get_element_text_on_opened_reg_tab(self):
        self.timeout = 20
        self.element_is_visible(RelatedPagesElementsLocators.REG_START_PAGE_TEXT)
        return self.get_text(RelatedPagesElementsLocators.REG_START_PAGE_TEXT)

    @allure.step("Get attribute 'href' of the REG.RU link")
    def get_reg_link_href(self):
        return self.get_link_href(FooterLocators.REG_LINK)

    @allure.step('Check the REG.RU image is present and visible in Footer')
    def check_reg_image_visibility(self):
        return self.element_is_visible(FooterLocators.REG_IMAGE)

    @allure.step('Get attribute "src" of the REG.RU image in Footer')
    def get_reg_image_src(self):
        return self.get_image_src(FooterLocators.REG_IMAGE)

    @allure.step('Get attribute "alt" of the REG.RU image in Footer')
    def get_reg_image_alt(self):
        return self.get_image_alt(FooterLocators.REG_IMAGE)

    @allure.step('Check the Selectel link is present and visible in Footer')
    def check_selectel_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.SELECTEL_LINK)

    @allure.step('Check the Selectel link is clickable in Footer')
    def check_selectel_link_clickability(self):
        return self.element_is_clickable(FooterLocators.SELECTEL_LINK)

    @allure.step("Get attribute 'href' of the Selectel link")
    def get_selectel_link_href(self):
        return self.get_link_href(FooterLocators.SELECTEL_LINK)

    @allure.step('Check the Selectel image is present and visible in Footer')
    def check_selectel_image_visibility(self):
        return self.element_is_visible(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Get attribute "src" of the Selectel image in Footer')
    def get_selectel_image_src(self):
        return self.get_image_src(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Get attribute "alt" of the Selectel image in Footer')
    def get_selectel_image_alt(self):
        return self.get_image_alt(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Check the Contact us link is present and visible in Footer')
    def check_contact_us_link_presence_and_visibility(self):
        return self.element_is_visible(FooterLocators.CONTACT_US_LINK)

    @allure.step('Check the Contact us link is clickable in Footer')
    def check_contact_us_link_clickability(self):
        return self.element_is_clickable(FooterLocators.CONTACT_US_LINK)

    @allure.step("Get attribute 'href' of the Contact us link")
    def get_contact_us_link_href(self):
        return self.get_link_href(FooterLocators.CONTACT_US_LINK)

    @allure.step("Check the prefix and the subject in the attribute 'href' of the Contact us link")
    def check_contact_us_link_href(self):
        link_href = self.get_contact_us_link_href()
        return "mailto" in link_href, "subject=BrainUp" in link_href
