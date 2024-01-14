import allure
from pages.base_page import BasePage
from test_data.links import MainPageLinks


class LoginPage(BasePage):

    def login_user(self):
        with allure.step(f'Check expected link {MainPageLinks.URL_GROUPS_PAGE}'):
            self.check_expected_link(MainPageLinks.URL_GROUPS_PAGE)
        with allure.step(f'Check current url is: {self.driver.current_url}.'):
            return self.driver.current_url
