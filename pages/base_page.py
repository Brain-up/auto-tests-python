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

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

