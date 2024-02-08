import allure
from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.used_resources_page_locators import UsedResourcesPageLocators


class UsedResourcesPage(BasePage):
    locators = UsedResourcesPageLocators

    @allure.step("Open the 'Used resources' page")
    def open_used_resources_page(self):
        self.driver.get(MainPageLinks.URL_USED_RESOURCES_PAGE)

    @allure.step('Check the page title is present in DOM')
    def check_used_resources_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step('Check the page title is visible on the page')
    def check_used_resources_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step('Get content of the title on the page')
    def get_used_resources_page_title_content(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    @allure.step('Check the page text is present in DOM')
    def check_used_resources_page_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step('Check the page text is visible on the page')
    def check_used_resources_page_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step('Get content of the text on the page')
    def get_text_content_on_the_used_resources_page(self):
        return self.element_is_visible(self.locators.PAGE_TEXT).text


