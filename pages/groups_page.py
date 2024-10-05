"""Methods for verifying web elements on the 'Groups' page"""
import allure
from pages.base_page import BasePage
from locators.groups_page_locators import GroupsPageLocators


class GroupsPage(BasePage):
    locators = GroupsPageLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)
