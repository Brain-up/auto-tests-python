import allure
from test_data.links import MainPageLinks


@allure.epic("Login Page.")
class TestLoginPage:

    @allure.title('Test for authorization customer.')
    def test_logining_user(self, driver, auto_test_user_authorized):
        login_page_url = driver.current_url
        assert login_page_url == MainPageLinks.URL_GROUPS_PAGE, "The link leads to an incorrect page"
