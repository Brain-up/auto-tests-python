import allure

from pages.base_page import BasePage
from test_data.links import MainPageLinks
from locators.used_resources_page_locators import UsedResourcesPageLocators, RelatedPagesElementsLocators


class UsedResourcesPage(BasePage):
    locators = UsedResourcesPageLocators
    locators1 = RelatedPagesElementsLocators

    @allure.step("Open the 'Used resources' page")
    def open_used_resources_page(self):
        self.driver.get(MainPageLinks.URL_USED_RESOURCES_PAGE)

    @allure.step("Check the page title is present in DOM")
    def check_used_resources_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the page title is visible on the page")
    def check_used_resources_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get content of the title on the page")
    def get_used_resources_page_title_content(self):
        return self.element_is_visible(self.locators.PAGE_TITLE).text

    @allure.step("Check the page text is present in DOM")
    def check_used_resources_page_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the page text is visible on the page")
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

    @allure.step('Check if the section with the freepik.com link is present in DOM')
    def check_presence_of_freepik_com_link_section(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK_SECTION)

    @allure.step('Check if the section with the freepik.com link is visible on the page')
    def check_visibility_of_freepik_com_link_section(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_LINK_SECTION)

    @allure.step('Check the freepik.com link is present in DOM')
    def check_freepik_com_link_presence(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK)

    @allure.step('Check the freepik.com link is visible on the page')
    def check_freepik_com_link_visibility(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_LINK)

    @allure.step('Check the freepik.com link is clickable')
    def check_freepik_com_link_clickability(self):
        return self.element_is_clickable(self.locators.FREEPIK_COM_LINK)

    @allure.step('Click on the freepik.com link and thereby open the corresponding web page in a new tab')
    def click_freepik_com_link(self):
        self.element_is_present_and_clickable(self.locators.FREEPIK_COM_LINK).click()

    @allure.step("Get text of the element on the freepik.com page")
    def get_element_text_on_opened_freepik_com_tab(self):
        return self.get_text(self.locators1.FREEPIK_COM_TEXT)

    @allure.step("Get attribute 'href' of the freepik.com link")
    def get_freepik_com_link_href(self):
        return self.get_link_href(self.locators.FREEPIK_COM_LINK)

    @allure.step('Get content of the text in the freepik.com link')
    def get_text_in_freepik_com_link(self):
        return self.element_is_present(self.locators.FREEPIK_COM_LINK).text

    @allure.step("Check the icon is present in freepik.com link's section")
    def check_icon_presence_in_freepik_com_section(self):
        return self.element_is_present(self.locators.FREEPIK_COM_SECTION_ICON)

    @allure.step("Check the icon is visible in freepik.com link's section")
    def check_icon_visibility_in_freepik_com_section(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_SECTION_ICON)

    @allure.step("Get attribute 'xmlns' of the icon in the freepik.com link's section")
    def get_icon_xmlns_in_freepik_com_section(self):
        return self.driver.find_element(*self.locators.FREEPIK_COM_SECTION_ICON).get_attribute("xmlns")

    @allure.step("Get attribute 'width' of the icon in freepik.com link's section")
    def get_width_of_icon_in_freepik_com_section(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_SECTION_ICON).get_attribute('width')

    @allure.step("Get attribute 'height' of the icon in freepik.com link's section")
    def get_height_of_icon_in_freepik_com_section(self):
        return self.element_is_visible(self.locators.FREEPIK_COM_SECTION_ICON).get_attribute('height')

    @allure.step('Check if the section with the "Plants" link is present in DOM')
    def check_presence_of_plants_link_section(self):
        return self.element_is_present(self.locators.PLANTS_LINK_SECTION)

    @allure.step('Check if the section with the "Plants" link is visible on the page')
    def check_visibility_of_plants_link_section(self):
        return self.element_is_visible(self.locators.PLANTS_LINK_SECTION)

    @allure.step("Check the 'Plants' link is present in DOM")
    def check_plants_link_presence(self):
        return self.element_is_present(self.locators.PLANTS_LINK)

    @allure.step("Check the 'Plants' link is visible on the page")
    def check_plants_link_visibility(self):
        return self.element_is_visible(self.locators.PLANTS_LINK)

    @allure.step("Check the 'Plants' link is clickable")
    def check_plants_link_clickability(self):
        return self.element_is_clickable(self.locators.PLANTS_LINK)

    @allure.step("Click on the 'Plants' link and thereby open the corresponding web page in a new tab")
    def click_plants_link(self):
        self.element_is_present_and_clickable(self.locators.PLANTS_LINK).click()

    @allure.step("Get text of the element on the 'Plants' page")
    def get_element_text_on_opened_plants_tab(self):
        return self.get_text(self.locators1.PLANTS_TEXT)

    @allure.step("Get attribute 'href' of the 'Plants' link")
    def get_plants_link_href(self):
        return self.get_link_href(self.locators.PLANTS_LINK)

    @allure.step("Get content of the text in the 'Plants' link")
    def get_text_in_plants_link(self):
        return self.element_is_present(self.locators.PLANTS_LINK).text
