"""Methods for verifying web elements on the starting page for unauthorized users"""
import allure

from pages.base_page import BasePage
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators


class StartUnauthorizedPage(BasePage):
    locators = StartUnauthorizedPageLocators

    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.UNAUTH_START_PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.UNAUTH_START_PAGE_CONTENT)

    @allure.step("Get amount of sections with content on the page")
    def get_amount_of_sections_on_page(self):
        sections = self.elements_are_present(self.locators.UNAUTH_START_PAGE_SECTIONS)
        return len(sections)

    @allure.step("Check the page title 01 is present in DOM")
    def check_start_unauthorized_page_title_01_presence(self):
        return self.element_is_present(self.locators.UNAUTH_START_PAGE_TITLE_1)

    @allure.step("Check the page title 01 is visible on the page")
    def check_start_unauthorized_page_title_01_visibility(self):
        return self.element_is_visible(self.locators.UNAUTH_START_PAGE_TITLE_1)

    @allure.step("Get content of the title 01 on the page")
    def get_content_of_title_01_on_start_unauthorized_page(self):
        return self.get_text(self.locators.UNAUTH_START_PAGE_TITLE_1)

    @allure.step("Check the text 01 is present in DOM")
    def check_start_unauthorized_page_text_01_presence(self):
        return self.element_is_present(self.locators.UNAUTH_START_PAGE_TEXT_1)

    @allure.step("Check the text 01 is visible on the page")
    def check_start_unauthorized_page_text_01_visibility(self):
        return self.element_is_visible(self.locators.UNAUTH_START_PAGE_TEXT_1)

    @allure.step("Get content of the text 01 on the page")
    def get_content_of_text_01_on_start_unauthorized_page(self):
        return self.get_text(self.locators.UNAUTH_START_PAGE_TEXT_1)
