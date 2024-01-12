import allure

from locators.footer_page_locators import FooterLocators
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

    @allure.step('Check Jetbrains image is present in the DOM tree on the page')
    def check_jetbrains_image_presence(self):
        return self.element_is_present(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check Jetbrains image is present and visible in Footer')
    def check_jetbrains_image_visibility(self):
        return self.element_is_visible(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check Jetbrains image is invisible in Footer')
    def check_jetbrains_image_invisibility(self):
        return self.element_is_not_visible(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Get attribute "src" of Jetbrains image in Footer')
    def get_jetbrains_image_src(self):
        return self.get_image_src(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Get attribute "alt" of Jetbrains image in Footer')
    def get_jetbrains_image_alt(self):
        return self.get_image_alt(FooterLocators.JETBRAINS_IMAGE)

    @allure.step('Check REG.RU image is present and visible in Footer')
    def check_reg_image_visibility(self):
        return self.element_is_visible(FooterLocators.REG_IMAGE)

    @allure.step('Get attribute "src" of REG.RU image in Footer')
    def get_reg_image_src(self):
        return self.get_image_src(FooterLocators.REG_IMAGE)

    @allure.step('Get attribute "alt" of REG.RU image in Footer')
    def get_reg_image_alt(self):
        return self.get_image_alt(FooterLocators.REG_IMAGE)

    @allure.step('Check ARASAAC image is present and visible in Footer')
    def check_arasaac_image_visibility(self):
        return self.element_is_visible(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Get attribute "src" of ARASAAC image in Footer')
    def get_arasaac_image_src(self):
        return self.get_image_src(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Get attribute "alt" of ARASAAC image in Footer')
    def get_arasaac_image_alt(self):
        return self.get_image_alt(FooterLocators.ARASAAC_IMAGE)

    @allure.step('Check Selectel image is present and visible in Footer')
    def check_selectel_image_visibility(self):
        return self.element_is_visible(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Get attribute "src" of Selectel image in Footer')
    def get_selectel_image_src(self):
        return self.get_image_src(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Get attribute "alt" of Selectel image in Footer')
    def get_selectel_image_alt(self):
        return self.get_image_alt(FooterLocators.SELECTEL_IMAGE)

    @allure.step('Check EPAM image is present and visible in Footer')
    def check_epam_image_visibility(self):
        return self.element_is_visible(FooterLocators.EPAM_IMAGE)

    @allure.step('Get attribute "src" of EPAM image in Footer')
    def get_epam_image_src(self):
        return self.get_image_src(FooterLocators.EPAM_IMAGE)

    @allure.step('Get attribute "alt" of EPAM image in Footer')
    def get_epam_image_alt(self):
        return self.get_image_alt(FooterLocators.EPAM_IMAGE)

    @allure.step("Get attribute 'href' of the Jetbrains link")
    def get_jetbrains_link_href(self):
        return self.get_link_href(FooterLocators.JETBRAINS_LINK)

    @allure.step("Get attribute 'href' of the REG.RU link")
    def get_reg_link_href(self):
        return self.get_link_href(FooterLocators.REG_LINK)

    @allure.step("Get attribute 'href' of the ARASAAC link")
    def get_arasaac_link_href(self):
        return self.get_link_href(FooterLocators.ARASAAC_LINK)
