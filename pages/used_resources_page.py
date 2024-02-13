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

    @allure.step('Check if the section with links is present in DOM')
    def check_presence_of_links_section_on_used_resources_page(self):
        return self.element_is_present(self.locators.LINKS_SECTION)

    @allure.step('Check if the section with links is visible on the page')
    def check_visibility_of_links_section_on_used_resources_page(self):
        return self.element_is_visible(self.locators.LINKS_SECTION)

    @allure.step('Check the freepik.com link is present in DOM')
    def check_freepik_com_link_presence(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK)

    @allure.step('Check the freepik.com link is visible on the page')
    def check_freepik_com_link_visibility(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_LINK)

    @allure.step('Check the freepik.com link is clickable')
    def check_freepik_com_link_clickability(self):
        return self.element_is_clickable(self.locators.FREEPIK_COM_LINK)

    @allure.step("Get attribute 'href' of the freepik.com link")
    def get_freepik_com_link_href(self):
        return self.get_link_href(self.locators.FREEPIK_COM_LINK)
