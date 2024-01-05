import allure

from locators.locators import FooterLocators
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
