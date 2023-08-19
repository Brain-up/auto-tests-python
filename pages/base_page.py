from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver import Keys
from locators.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators()

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def open_page(self):
        self.driver.get(self.link)

    def click_header_link(self, link_name):
        match link_name:
            case 'description':
                self.driver.find_element(*self.locators.DESCRIPTION_PAGE).click()

    def check_header_link(self, link_name):
        self.click_header_link(link_name)
        assert link_name in self.driver.current_url

    def element_is_displayed(self, locator, wait):
        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    def link_visible_and_clickable(self, locator):
        """
        В случае ошибки подставляет в ответ адрес несработавшей ссылки
        """
        link = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        link_text = link.get_attribute('href')
        assert link.is_displayed() and link.is_enabled(), \
            f'"{link_text}" link is not visible or clickable'