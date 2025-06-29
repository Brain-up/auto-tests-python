"""Methods for verifying web elements on the 'Groups' page"""
import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from pages.base_page import BasePage
from locators.groups_page_locators import GroupsPageLocators, HeaderLocators
from test_data.links import MainPageLinks as Links


class GroupsPage(BasePage):
    locators = GroupsPageLocators
    locators1 = HeaderLocators

    # Checking the structure and display of elements on the page
    @allure.step("Check if some content is present in DOM")
    def check_presence_of_page_content(self):
        return self.element_is_present(self.locators.PAGE_CONTENT)

    @allure.step("Check if page content is visible on the page")
    def check_visibility_of_page_content(self):
        return self.element_is_visible(self.locators.PAGE_CONTENT)

    @allure.step("Get structure of the 1st level of nesting on the page")
    def get_structure_of_1st_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_FIRST_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 1st level of nesting are visible")
    def check_elements_visibility_on_1st_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_1st_level())

    @allure.step("Get structure of the 2nd level of nesting on the page")
    def get_structure_of_2nd_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        # tags = [element.tag_name for element in elements]
        return self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        elements = self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)
        # tags = [element.tag_name for element in elements]
        return elements

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level(self):
        elements = self.get_structure_of_6th_level()
        return all(element.is_displayed() for element in elements)

    @allure.step("Check the title h3 on the 2nd level of nesting is present on the page")
    def check_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the title h3 on the 2nd level of nesting is visible")
    def check_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get the list of tiles on the 2nd level of nesting on the page")
    def get_list_of_tiles(self):
        return self.elements_are_present(self.locators.PAGE_TILES)

    @allure.step("Check if tiles on the 2nd level of nesting are visible")
    def check_visibility_of_tiles(self):
        return all(element.is_displayed() for element in self.get_list_of_tiles())

    @allure.step("Get the list of images on the 6th level of nesting on the page")
    def get_list_of_images(self):
        elements = self.elements_are_present(self.locators.PAGE_IMAGES)
        return elements

    @allure.step("Check if images on the 6th level of nesting are visible")
    def check_visibility_of_images(self):
        elements = self.get_list_of_images()
        return all(element.is_displayed() for element in elements)

    @allure.step("Get the list of subtitles on the 6th level of nesting on the page")
    def get_list_of_subtitles(self):
        return self.elements_are_present(self.locators.PAGE_SUBTITLES)

    @allure.step("Check if subtitles on the 6th level of nesting are visible")
    def check_visibility_of_subtitles(self):
        return all(element.is_displayed() for element in self.get_list_of_subtitles())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab on the 'ru' local")
    def get_value_of_tab_title_ru(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title of the tab on the 'en' local")
    def get_value_of_tab_title_en(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the title with tag 'h3' on the 'ru' local")
    def get_value_of_page_title_ru(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Get value of the title with tag 'h3' on the 'en' local")
    def get_value_of_page_title_en(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Get the list of subtitle 'h4' values on the 'ru' local")
    def get_values_of_subtitles_ru(self):
        elements = self.get_list_of_subtitles()
        Wait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.locators.PAGE_SUBTITLES))
        return [element.text for element in elements]

    @allure.step("Get the list of subtitle 'h4' values on the 'en' local")
    def get_values_of_subtitles_en(self):
        return [element.text for element in self.get_list_of_subtitles()]

    @allure.step("Get the list of links on the 3rd level of nesting on the page")
    def get_list_of_links(self):
        return self.elements_are_present(self.locators.PAGE_LINKS)

    @allure.step("Check if links on the 3rd level of nesting are visible")
    def check_visibility_of_links(self):
        return all(element.is_displayed() for element in self.get_list_of_links())

    @allure.step("Check if links are clickable")
    def check_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list_of_links())

    @allure.step("Get attribute 'title' of links on the 'ru' local")
    def get_links_titles_ru(self):
        elements = self.get_list_of_links()
        return [element.get_attribute('title') for element in elements]

    @allure.step("Get attribute 'title' of links on the 'en' local")
    def get_links_titles_en(self):
        return [element.get_attribute("title") for element in self.get_list_of_links()]

    @allure.step("Get attribute 'href' of links on the 'ru' local")
    def get_links_href_ru(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Get attribute 'href' of links on the 'en' local")
    def get_links_href_en(self):
        return [element.get_attribute("href") for element in self.get_list_of_links()]

    @allure.step("Check the first part of the attribute 'href' of links")
    def check_first_part_of_link_href(self):
        link_href = self.get_link_href(self.locators.PAGE_LINKS)
        return link_href.startswith(f'{Links.URL_MAIN_PAGE}groups/')

    @allure.step("Get status code of links")
    def get_links_status_codes(self):
        return [requests.head(link_href).status_code for link_href in self.get_links_href_ru()]

    @allure.step("Click on links on the 'ru' local and thereby open corresponding web pages in the same tab")
    def click_on_links_on_ru_local(self):
        opened_pages = []

        link1 = self.element_is_present_and_clickable(self.locators.PAGE_LINK1)
        current_url = self.driver.current_url
        link1.click()
        Wait(self.driver, 10).until(EC.url_changes(current_url))
        opened_pages.append(self.get_current_tab_url())
        self.element_is_present_and_clickable(self.locators1.LOGO_LINK).click()
        link2 = self.element_is_present_and_clickable(self.locators.PAGE_LINK2)
        current_url = self.driver.current_url
        link2.click()
        Wait(self.driver, 10).until(EC.url_changes(current_url))
        opened_pages.append(self.get_current_tab_url())

        return opened_pages

    @allure.step("Click on links on the 'en' local and thereby open corresponding web pages in the same tab")
    def click_on_links_on_en_local(self):
        opened_pages = []

        link1 = self.element_is_present_and_clickable(self.locators.PAGE_LINK1)
        current_url = self.driver.current_url
        link1.click()
        Wait(self.driver, 10).until(EC.url_changes(current_url))
        opened_pages.append(self.get_current_tab_url())

        self.driver.back()
        Wait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))

        link2 = self.element_is_present_and_clickable(self.locators.PAGE_LINK2)
        current_url = self.driver.current_url
        link2.click()
        Wait(self.driver, 10).until(EC.url_changes(current_url))
        opened_pages.append(self.get_current_tab_url())

        return opened_pages

    # Checking images on the page
    @allure.step("Get the list of attribute 'src' values of images in links")
    def get_images_src(self):
        return [image.get_attribute('src') for image in self.get_list_of_images()]

    @allure.step("Get the list of attribute 'alt' values of images in links on the 'ru' local")
    def get_images_alt_ru(self):
        elements = self.get_list_of_images()
        return [element.get_attribute('alt') for element in elements]

    @allure.step("Get the list of attribute 'alt' values of images in links on the 'en' local")
    def get_images_alt_en(self):
        return [image.get_attribute('alt') for image in self.get_list_of_images()]

    @allure.step("Get the list of sizes of images in links")
    def get_images_sizes(self):
        elements = self.get_list_of_images()
        return [element.size for element in elements]

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images(self):
        images = self.get_list_of_images()
        before = [img.size for img in images]
        self.driver.set_window_size(400, 700)

        Wait(self.driver, 5).until(lambda d: any(before[i] != img.size for i, img in enumerate(images)))

        after = [img.size for img in images]
        return {
            'changed': [i for i, (b, a) in enumerate(zip(before, after)) if b != a and a != {'height': 0, 'width': 0}],
            'unchanged': [i for i, (b, a) in enumerate(zip(before, after)) if b == a],
            'lost': [i for i, a in enumerate(after) if a == {'height': 0, 'width': 0}]
        }
