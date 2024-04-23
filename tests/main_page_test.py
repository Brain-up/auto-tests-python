import allure

from pages.main_page import MainPage
from test_data.links import MainPageLinks


@allure.epic("Main Page.")
class TestMainPage:

    @allure.title("Verify redirection to description page not authorized user.")
    def test_mp_01_verify_redirection_to_description_page(self, driver, main_page_open):
        page = MainPage(driver)
        description_url = page.open_description_page()
        assert description_url == MainPageLinks.URL_DESCRIPTION_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to telegram page not authorized user.")
    def test_mp_02_verify_redirection_to_telegram_page(self, driver, main_page_open):
        page = MainPage(driver)
        telegram_url = page.open_telegram_page()
        assert telegram_url == MainPageLinks.URL_TELEGRAM_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to donate page not authorized user.")
    def test_mp_03_verify_redirection_to_donate_page(self, driver, main_page_open):
        page = MainPage(driver)
        donate_url = page.open_donate_page()
        assert donate_url == MainPageLinks.URL_DONATE_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to contacts page not authorized user.")
    def test_mp_04_verify_redirection_to_contacts_page(self, driver, main_page_open):
        page = MainPage(driver)
        contacts_page_url = page.open_contacts_page()
        assert contacts_page_url == MainPageLinks.URL_CONTACTS_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to specialists page not authorized user.")
    def test_mp_05_verify_redirection_to_specialists_page(self, driver, main_page_open):
        page = MainPage(driver)
        specialists_page_url = page.open_specialists_page()
        assert specialists_page_url == MainPageLinks.URL_SPECIALISTS_PAGE, \
            (f"The link leads to an incorrect page. \nExpected link: {MainPageLinks.URL_SPECIALISTS_PAGE}."
             f"\nGotten link: {specialists_page_url}.")

    @allure.title("Verify redirection to github not authorized user.")
    def test_mp_06_verify_redirection_to_github(self, driver, main_page_open):
        page = MainPage(driver)
        github_page_url = page.open_github()
        assert github_page_url == MainPageLinks.URL_GITHUB, "The link leads to an incorrect page."

    @allure.title("Verify redirection to contributors page not authorized user.")
    def test_mp_07_verify_redirection_to_contributors_page(self, driver, main_page_open):
        page = MainPage(driver)
        contributors_page_url = page.open_contributors_page()
        assert contributors_page_url == MainPageLinks.URL_CONTRIBUTORS_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to used resources page not authorized user.")
    def test_mp_08_verify_redirection_to_used_resources_page(self, driver, main_page_open):
        page = MainPage(driver)
        resources_page_url = page.open_used_resources_page()
        assert resources_page_url == MainPageLinks.URL_USED_RESOURCES_PAGE, "The link leads to an incorrect page."

    @allure.title("Checking the clickability of the Start button.")
    def test_mp_9_checking_the_clickability_of_the_start_button(self, driver, main_page_open):
        page = MainPage(driver)
        start_button = page.clickability_of_the_start_button()
        assert start_button == MainPageLinks.URL_LOGIN_PAGE, "The link leads to an incorrect page."

    @allure.title("Checking the clickability of the Registration button.")
    def test_mp_10_checking_clickability_of_the_registration_button(self, driver, main_page_open):
        page = MainPage(driver)
        registration_button = page.clicability_of_registration_button()
        assert registration_button == MainPageLinks.URL_REGISTRATION_PAGE, "The link leads to an incorrect page."

