"""Methods for verifying web elements on the 'Exercises "Similar phrases"' page on the 'ru' local"""
import allure
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait
from pages.base_page import BasePage
from locators.exercises_ru_similar_phrases_page_locators import ExercisesRuSimilarPhrasesPageLocators


class ExercisesRuSimilarPhrasesPage(BasePage):
    locators = ExercisesRuSimilarPhrasesPageLocators

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
        return self.elements_are_present(self.locators.PAGE_SECOND_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 2nd level of nesting are visible")
    def check_elements_visibility_on_2nd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_2nd_level())

    @allure.step("Get structure of the 3rd level of nesting on the page")
    def get_structure_of_3rd_level(self):
        return self.elements_are_present(self.locators.PAGE_THIRD_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 3rd level of nesting are visible")
    def check_elements_visibility_on_3rd_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_3rd_level())

    @allure.step("Get structure of the 4th level of nesting on the page")
    def get_structure_of_4th_level(self):
        return self.elements_are_present(self.locators.PAGE_FOURTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 4th level of nesting are visible")
    def check_elements_visibility_on_4th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_4th_level())

    @allure.step("Get structure of the 5th level of nesting on the page")
    def get_structure_of_5th_level(self):
        return self.elements_are_present(self.locators.PAGE_FIFTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 5th level of nesting are visible")
    def check_elements_visibility_on_5th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_5th_level())

    @allure.step("Get structure of the 6th level of nesting on the page")
    def get_structure_of_6th_level(self):
        return self.elements_are_present(self.locators.PAGE_SIXTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 6th level of nesting are visible")
    def check_elements_visibility_on_6th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_6th_level())

    @allure.step("Get structure of the 7th level of nesting on the page")
    def get_structure_of_7th_level(self):
        return self.elements_are_present(self.locators.PAGE_SEVENTH_LEVEL_ELEMENTS)

    @allure.step("Check if elements of the 7th level of nesting are visible")
    def check_elements_visibility_on_7th_level(self):
        return all(element.is_displayed() for element in self.get_structure_of_7th_level())

    @allure.step("Check the list1 on the 5th level of nesting is present on the page")
    def get_list1_of_breadcrumbs_links(self):
        return self.elements_are_present(self.locators.PAGE_LIST1)

    @allure.step("Check the list1 is visible")
    def check_list1_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST1)

    @allure.step("Check the list2 on the 5th level of nesting is present on the page")
    def get_list2_of_group_links(self):
        return self.elements_are_present(self.locators.PAGE_LIST2)

    @allure.step("Check the list2 is visible")
    def check_list2_visibility(self):
        return self.element_is_visible(self.locators.PAGE_LIST2)

    @allure.step("Check the list3 on the 5th level of nesting is present on the page")
    def get_list3_of_series_links(self):
        return self.elements_are_present(self.locators.PAGE_LIST3)

    @allure.step("Check the list3 is visible")
    def check_list3_visibility(self):
        return all(element.is_displayed() for element in self.get_list3_of_series_links())

    @allure.step("Check the list4 on the 6th level of nesting is present on the page")
    def get_list4_of_links(self):
        return self.elements_are_present(self.locators.CARD_IMAGES_LIST4)

    @allure.step("Check the list4 is visible")
    def check_list4_visibility(self):
        return all(element.is_displayed() for element in self.get_list4_of_links())

    # Checking text on the tab&page
    @allure.step("Get value of the title of the tab")
    def get_value_of_tab_title(self):
        return self.get_current_tab_title()

    @allure.step("Get value of the breadcrumbs on the page")
    def get_value_of_breadcrumbs(self):
        # print(len(breadcrumbs_text), breadcrumbs_text, sep='\n')
        return [element.text for element in self.get_list1_of_breadcrumbs_links()]

    @allure.step("Get text in group links on the page")
    def get_group_links_text(self):
        return [element.text for element in self.get_list2_of_group_links()]

    @allure.step("Get text in series links on the page")
    def get_series_links_text(self):
        return [element.text for element in self.get_list3_of_series_links()]

    # Checking links on the page
    @allure.step("Check if breadcrumbs are clickable")
    def check_breadcrumbs_clickability(self):
        return all(link.is_enabled() for link in self.get_list1_of_breadcrumbs_links())

    @allure.step("Get attribute 'href' of links in breadcrumbs")
    def get_breadcrumbs_links_href(self):
        # print(len(breadcrumbs_links_href), *breadcrumbs_links_href, sep='\n')
        return [element.get_attribute("href") for element in self.get_list1_of_breadcrumbs_links()]

    @allure.step("Get status code of links in breadcrumbs")
    def get_link_status_codes_in_breadcrumbs(self):
        return [requests.head(link_href).status_code for link_href in self.get_breadcrumbs_links_href()]

    @allure.step("Check if group links are clickable")
    def check_group_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list2_of_group_links())

    @allure.step("Get attribute 'title' of group links")
    def get_group_link_titles(self):
        # print(len(group_link_titles), *group_link_titles, sep='\n')
        return [element.get_attribute("title") for element in self.get_list2_of_group_links()]

    @allure.step("Get attribute 'active-links' of group links")
    def get_group_link_active_links(self):
        # print(len(group_link_active_links), *group_link_active_links, sep='\n')
        return [el.get_attribute("data-test-active-link") for el in self.get_list2_of_group_links()]

    @allure.step("Check if series links are clickable")
    def check_series_links_clickability(self):
        return all(link.is_enabled() for link in self.get_list3_of_series_links())

    @allure.step("Get attribute 'href' of series links")
    def get_series_links_href(self):
        # print(len(series_links_href), *series_links_href, sep='\n')
        return [element.get_attribute("href") for element in self.get_list3_of_series_links()]

    @allure.step("Get status code of series links")
    def get_series_link_status_codes(self):
        return [requests.head(link_href).status_code for link_href in self.get_series_links_href()]

    @allure.step("Click on breadcrumbs links and thereby open corresponding web pages in the same tab")
    def click_on_breadcrumbs_links(self):
        breadcrumbs_locators = [self.locators.PAGE_LIST1_1, self.locators.PAGE_LIST1_2, self.locators.PAGE_LIST1_3]
        group_page_url = self.get_current_tab_url()
        opened_pages = [self.get_current_tab_url()]

        for link_locator in breadcrumbs_locators[:2]:
            self.element_is_clickable(link_locator).click()
            Wait(self.driver, self.timeout).until(EC.url_changes(group_page_url))
            opened_pages.append(self.get_current_tab_url())
            self.driver.back()
            Wait(self.driver, self.timeout).until(EC.url_to_be(group_page_url))

        return opened_pages

    @allure.step("Click on group links and thereby open corresponding web pages in the same tab")
    def click_on_group_links(self):
        group_links = self.get_list2_of_group_links()
        opened_pages = []

        for link in group_links:
            link.click()
            Wait(self.driver, self.timeout).until(EC.url_changes(self.get_current_tab_url()))
            opened_pages.append(self.get_current_tab_url())

        return opened_pages

    @allure.step("""Click on series links and thereby open corresponding web pages in the same tab""")
    def click_on_series_links(self):
        series_locators = [self.locators.PAGE_LIST3_1, self.locators.PAGE_LIST3_2,
                           self.locators.PAGE_LIST3_3, self.locators.PAGE_LIST3_4,
                           self.locators.PAGE_LIST3_5, self.locators.PAGE_LIST3_6]
        group_page_url = self.get_current_tab_url()
        opened_pages = []

        for link_locator in series_locators:
            self.element_is_clickable(link_locator).click()
            Wait(self.driver, self.timeout).until(EC.url_changes(group_page_url))
            opened_pages.append(self.get_current_tab_url())
            self.driver.back()
            Wait(self.driver, self.timeout).until(EC.url_to_be(group_page_url))

        # print(*opened_pages, sep='\n')
        return opened_pages

    # Checking images on the page
    @allure.step("Get the list of attribute 'style' values of images in links")
    def get_links_style(self):
        style = [image.get_attribute('style') for image in self.get_list4_of_links()]
        # print(len(style), *style, sep='\n')
        return style

    @allure.step("Get the list of sizes of background-images in links")
    def get_images_sizes(self):
        images_size = [image.size for image in self.get_list4_of_links()]
        # print(len(images_size), *images_size, sep='\n')
        return images_size

    @allure.step("Check changes of images sizes after resizing")
    def check_size_changes_of_images(self):
        images = self.get_list4_of_links()
        before = [img.size for img in images]
        self.driver.set_window_size(400, 700)

        Wait(self.driver, 5).until(lambda d: any(before[i] != img.size for i, img in enumerate(images)))

        after = [img.size for img in images]
        return {
            'changed': [i for i, (b, a) in enumerate(zip(before, after)) if b != a and a != {'height': 0, 'width': 0}],
            'unchanged': [i for i, (b, a) in enumerate(zip(before, after)) if b == a],
            'lost': [i for i, a in enumerate(after) if a == {'height': 0, 'width': 0}]
        }
