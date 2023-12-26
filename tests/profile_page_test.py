import allure
from pages.profile_page import ProfilePage, get_link_change_password_by_email
from test_data.links import MainPageLinks


@allure.epic("Test Profile Page")
class TestProfilePage:
    urls = MainPageLinks

    @allure.title("Change the password by receiving an email link")
    def test_change_password(self, driver):
        page = ProfilePage(driver)
        driver.get(self.urls.URL_MAIN_PAGE)
        page.open_login_page()
        page.user_has_authorised()
        page.go_to_profile_page()
        page.click_change_password_link()
        page.field_recovery_email()
        page.click_send_recovery_email_link()
        link = get_link_change_password_by_email()
        driver.get(link)
        page.enter_new_password_field()
        page.click_save_button()
        page.get_successful_message()
        assert page.get_successful_message(), "The password hasn't changed"
