import allure

from locators.locators import BasePageLocators
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link
        self.timeout = 10

    def open(self):
        with allure.step(f'Open page: {self.link}'):
            self.driver.get(self.link)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)

    def element_is_presence_and_clickable(self, locator):
        with allure.step(f'Check element is visible and clickable: {locator}'):
            return (Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}") and
                    self.element_is_clickable(locator))

    def element_is_visible(self, locator):
        with allure.step(f'Check element is visible: {locator}'):
            self.go_to_element(self.element_is_presence(locator))
            return Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def elements_are_visible(self, locator):
        with allure.step(f'Check elements are visible: {locator}'):
            return Wait(self.driver, self.timeout).until(ec.visibility_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def element_is_presence(self, locator):
        with allure.step(f'Check element is presence: {locator}'):
            return Wait(self.driver, self.timeout).until(ec.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def elements_are_presence(self, locator):
        with allure.step(f'Check elements are presence: {locator}'):
            return Wait(self.driver, self.timeout).until(ec.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    @allure.step('Check element is clickable')
    def element_is_clickable(self, locator):
        with allure.step(f'Check elements are clickable: {locator}'):
            return Wait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def go_to_element(self, element):
        with allure.step(f'Go to element: {element}'):
            return self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center'});", element)

    def check_expected_link(self, url):
        with allure.step(f'Check url is presence: {url}'):
            return Wait(self.driver, self.timeout).until(ec.url_to_be(url),
                                                         message=f"Can't find element by locator {url}")

    def wait_changed_url(self, url):
        with allure.step(f'Wait until url: {url} will be changed.'):
            return Wait(self.driver, self.timeout).until(ec.url_changes(url),
                                                         message=f"Url: {url} has not been changed!!!")

    @allure.step('Get element text')
    def get_text(self, locator):
        text = self.element_is_visible(locator)
        return text.text
