import allure

from pages.base_page import BasePage
from locators.specialists_page_locators import SpecialistsPageLocators


class SpecialistsPage(BasePage):
    locators = SpecialistsPageLocators

    @allure.step("Check the page title is present in DOM")
    def check_specialists_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the page title is visible on the page")
    def check_specialists_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get content of the title on the page")
    def get_specialists_page_title_content(self):
        return self.get_text(self.locators.PAGE_TITLE)

    @allure.step("Check the page text is present in DOM")
    def check_specialists_page_text_presence(self):
        return self.element_is_present(self.locators.PAGE_TEXT)

    @allure.step("Check the text is visible on the page")
    def check_specialists_page_text_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TEXT)

    @allure.step("Get content of the text on the page")
    def get_text_content_on_the_specialists_page(self):
        return self.get_text(self.locators.PAGE_TEXT)

    @allure.step("Check the page grid is present in DOM")
    def check_specialists_page_grid_presence(self):
        return self.element_is_present(self.locators.PAGE_GRID)

    @allure.step("Check the page grid is visible on the page")
    def check_specialists_page_grid_visibility(self):
        return self.element_is_visible(self.locators.PAGE_GRID)

    @allure.step("Get the grid size on the page")
    def get_specialists_page_grid_size(self):
        grid = self.elements_are_present(self.locators.PAGE_GRID_CONTENT)
        return len(grid)
