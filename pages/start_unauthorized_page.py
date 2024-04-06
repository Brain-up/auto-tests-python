"""Methods for verifying web elements on the starting page for unauthorized users"""
import allure

from pages.base_page import BasePage
from locators.start_unauthorized_page_locators import StartUnauthorizedPageLocators


class StartUnauthorizedPage(BasePage):
    locators = StartUnauthorizedPageLocators

    @allure.step("Check the page title #1 is present in DOM")
    def check_start_unauthorized_page_title_01_presence(self):
        return self.element_is_present(self.locators.UNAUTH_START_PAGE_TITLE_1)

    @allure.step("Check the page title #1 is visible on the page")
    def check_start_unauthorized_page_title_01_visibility(self):
        return self.element_is_visible(self.locators.UNAUTH_START_PAGE_TITLE_1)

    @allure.step("Get content of the title #1 on the page")
    def get_content_of_title_01_on_start_unauthorized_page(self):
        return self.get_text(self.locators.UNAUTH_START_PAGE_TITLE_1)


