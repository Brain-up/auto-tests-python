"""Methods for verifying web elements in the Header on the site"""
import allure

from pages.base_page import BasePage
from locators.header_page_locators import HeaderPageLocators


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    @allure.step("Check if some content is present in the Header")
    def check_presence_of_header_content(self):
        return self.element_is_present(self.locators.HEADER_CONTENT)

    @allure.step("Check if page content is visible in the Header")
    def check_visibility_of_header_content(self):
        return self.element_is_visible(self.locators.HEADER_CONTENT)
