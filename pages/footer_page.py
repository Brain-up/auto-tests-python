import allure
from pages.base_page import BasePage


class FooterPage(BasePage):
    @allure.step('Find the element on the page')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Get attribute 'src' of an element's image")
    def get_image_src(self, locator):
        return self.driver.find_element(*locator).get_attribute("src")

    @allure.step("Get attribute 'alt' of an element's image")
    def get_image_alt(self, locator):
        return self.driver.find_element(*locator).get_attribute("alt")
