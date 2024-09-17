import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as Wait

from locators.main_page_locators import MainPageLocators


class BasePage:
    locators = MainPageLocators()

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link
        self.timeout = 20

    def open(self):
        with allure.step(f'Open page: {self.link}'):
            self.driver.get(self.link)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url: ' + get_url)
        return get_url

    def element_is_present_and_clickable(self, locator):
        return (Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}") and
                self.element_is_clickable(locator))

    def element_is_visible(self, locator):
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, self.timeout).until(
            ec.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def elements_are_visible(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.visibility_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}")

    def element_is_not_visible(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.invisibility_of_element_located(locator), message=f"The element located by {locator} is invisible")

    def element_is_present(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def elements_are_present(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def element_is_clickable(self, locator):
        return Wait(self.driver, self.timeout).until(
            ec.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView({ block: 'center'});", element)

    def check_expected_link(self, url):
        with allure.step(f'Check url is present: {url}'):
            try:
                return Wait(self.driver, self.timeout).until(
                    ec.url_to_be(url), message=f"Can't find element by locator {url}")
            except Exception as ex:
                print(ex)
                return Wait(self.driver, self.timeout).until(
                    ec.url_to_be(url), message=f"Can't find element by locator {url}")

    def wait_changed_url(self, url):
        with allure.step(f'Wait until url: {url} will be changed.'):
            Wait(self.driver, self.timeout).until(
                ec.url_changes(url), message=f"Url: {url} has not been changed!!!")

    def wait_url_to_be(self, url):
        with allure.step(f'Wait until url to be: {url}.'):
            Wait(self.driver, self.timeout).until(
                ec.url_to_be(url), message=f"Url: {url} has not been changed!!!")

    def get_text(self, locator):
        with allure.step(f'Get text in the element: {locator}'):
            return self.element_is_visible(locator).text

    def get_link_href(self, locator):
        return self.driver.find_element(*locator).get_attribute("href")

    def get_image_src(self, locator):
        return self.driver.find_element(*locator).get_attribute("src")

    def get_image_alt(self, locator):
        return self.driver.find_element(*locator).get_attribute("alt")

    def get_image_size(self, locator):
        return self.driver.find_element(*locator).size

    def get_current_tab_title(self):
        try:
            Wait(self.driver, 30).until(ec.presence_of_element_located((By.TAG_NAME, "title")))
            return self.driver.title
        except TimeoutException:
            return False

    def get_current_tab_url(self):
        try:
            Wait(self.driver, 50).until(ec.presence_of_element_located((By.TAG_NAME, "title")))
            return self.driver.current_url
        except TimeoutException:
            return False

    def element_is_not_clickable(self, locator):
        self.timeout = 5
        try:
            Wait(self.driver, self.timeout).until(ec.element_to_be_clickable(locator))
            return False
        except TimeoutException:
            return True

    def action_move_to_element(self, element):
        with allure.step('Action move to element'):
            with allure.step(f'Move to {element}'):
                action = ActionChains(self.driver)
                action.move_to_element(element)
                action.perform()

    def check_element_is_visible(self, locator):
        """Return True or False if element is visible it's more easily for asserts"""
        try:
            Wait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator),
                                             message=f"Can't find element by locator {locator}")
            return True
        except TimeoutException:
            return False
