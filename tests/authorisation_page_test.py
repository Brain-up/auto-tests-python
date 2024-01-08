import allure
from pages.profile_page import ProfilePage
from test_data.links import MainPageLinks
from test_data.data import Messages


@allure.epic("Test Authorized User Page")
class TestAuthorizedUserPage:
    urls = MainPageLinks
    msg = Messages

    @allure.title('Checking the possibility of authorization with the correct data')
    def test_auth_user_with_correct_data(self, driver, main_page_open):
        page = ProfilePage(driver)
        page.open_login_page()
        page.user_has_authorised()
        assert page.check_user_profile(), 'The user did not authorized with the correct data'

    @allure.title('Checking the possibility of authorization with incorrect data')
    def test_auth_user_with_wrong_password(self, driver, main_page_open):
        page = ProfilePage(driver)
        page.open_login_page()
        page.user_has_authorised_with_new_password()
        text = page.get_error_message()
        assert text == self.msg.WRONG_PASSWORD, 'The user authorized with incorrect data'
