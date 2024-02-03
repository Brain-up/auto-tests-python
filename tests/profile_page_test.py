import allure
from pages.profile_page import ProfilePage
from test_data.links import MainPageLinks


@allure.epic("Test Profile Page")
class TestProfilePage:
    urls = MainPageLinks
    page = ProfilePage

    @allure.title("Change the password by receiving an email link")
    def test_change_password(self, driver, main_page_open):
        page = ProfilePage(driver)
        page.open_login_page()
        page.user_has_authorised()
        page.go_to_profile_page()
        page.click_change_password_link()
        page.field_recovery_email()
        page.click_send_recovery_email_link()
        link = page.get_link_change_password_by_email()
        assert link, "The link to change the password was not received"
        driver.get(link)
        page.enter_new_password_field()
        page.click_save_button()
        page.get_successful_message()
        assert page.get_successful_message(), "The password hasn't changed"
        driver.back()
        # Return the password by receiving an email link
        page = ProfilePage(driver)
        page.open_login_page()
        page.user_has_authorised_with_new_password()
        page.go_to_profile_page()
        page.click_change_password_link()
        page.field_recovery_email()
        page.click_send_recovery_email_link()
        link = page.get_link_change_password_by_email()
        assert link, "The link to change the password was not received"
        driver.get(link)
        page.enter_old_password_field()
        page.click_save_button()
        page.get_successful_message()
        assert page.get_successful_message(), "The password hasn't changed"
