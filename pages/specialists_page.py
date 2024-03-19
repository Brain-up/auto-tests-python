import allure

from pages.base_page import BasePage
from locators.specialists_page_locators import SpecialistsPageLocators


class SpecialistsPage(BasePage):
    locators = SpecialistsPageLocators

    @allure.step("Check the 'Specialists' page title is present in DOM")
    def check_specialists_page_title_presence(self):
        return self.element_is_present(self.locators.PAGE_TITLE)

    @allure.step("Check the 'Specialists' page title is visible on the page")
    def check_specialists_page_title_visibility(self):
        return self.element_is_visible(self.locators.PAGE_TITLE)

    @allure.step("Get content of the title on the 'Specialists' page")
    def get_specialists_page_title_content(self):
        return self.get_text(self.locators.PAGE_TITLE)
