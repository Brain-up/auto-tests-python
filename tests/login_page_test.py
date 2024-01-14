import allure

from pages.login_page import LoginPage
from test_data.links import MainPageLinks


@allure.epic("Login Page.")
class TestLoginPage:

    @allure.title('Test for authorization customer.')
    def test_logining_user(self, driver, main_page_open):
        page = LoginPage(driver)
        login_page_url = page.login_user()
        assert login_page_url == MainPageLinks.URL_GROUPS_PAGE, "The link leads to an incorrect page"
