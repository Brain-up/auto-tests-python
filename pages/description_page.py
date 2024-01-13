import allure

from locators.description_page_locator import DescriptionPageLocators
from pages.base_page import BasePage
from test_data.links import MainPageLinks


class DescriptionPage(BasePage):
    locators = DescriptionPageLocators()

    @allure.step("Return main page from description page")
    def return_main_page(self):
        self.element_is_present_and_clickable(self.locators.LOGO).click()
        self.check_expected_link(MainPageLinks.URL_MAIN_PAGE)
        return self.driver.current_url

    @allure.step("Open telegram page")
    def transition_telegram_page(self):
        self.element_is_clickable(self.locators.TELEGRAM_PAGE).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_TELEGRAM_PAGE)
        return self.driver.current_url

    @allure.step("Open donate page")
    def transition_donate_page(self):
        self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_present_and_clickable(self.locators.DONATE_PAGE).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_DONATE_PAGE)
        return self.driver.current_url

    @allure.step("Open contacts page")
    def transition_contacts_page(self):
        self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_present_and_clickable(self.locators.CONTACTS).click()
        self.check_expected_link(MainPageLinks.URL_CONTACTS)
        return self.driver.current_url

    @allure.step("Open specialists page")
    def transition_specialists_page(self):
            self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
            self.element_is_present_and_clickable(self.locators.SPECIALISTS_PAGE).click()
            self.check_expected_link(MainPageLinks.URL_SPECIALISTS_PAGE)
            return self.driver.current_url

    @allure.step("Open github page")
    def transition_github(self):
        self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_present_and_clickable(self.locators.GITHUB).click()
        self.switch_to_new_window()
        self.check_expected_link(MainPageLinks.URL_GITHUB)
        return self.driver.current_url

    @allure.step("Open contributors page")
    def transition_contributors_page(self):
        self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_present_and_clickable(self.locators.CONTRIBUTORS_PAGE).click()
        self.check_expected_link(MainPageLinks.URL_CONTRIBUTORS_PAGE)
        return self.driver.current_url

    @allure.step("Open used resources page")
    def transition_used_resources_page(self):
        self.element_is_present_and_clickable(self.locators.MORE_MENU).click()
        self.element_is_present_and_clickable(self.locators.USED_RESOURCES_PAGE).click()
        self.check_expected_link(MainPageLinks.URL_USED_RESOURCES_PAGE)
        return self.driver.current_url

