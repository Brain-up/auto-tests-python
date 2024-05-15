import allure

from pages.description_page import DescriptionPage
from test_data.links import MainPageLinks


@allure.epic("Description Page.")
class TestDescriptionPage:
    @allure.title("Verify return main page from description page.")
    def test_dp_01_verify_return_main_page_from_description_page(self, driver, description_page_open):
        page = DescriptionPage(driver)
        main_url = page.return_main_page()
        assert main_url == MainPageLinks.URL_MAIN_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to telegram page not authorized user.")
    def test_dp_02_verify_redirection_to_telegram_page(self, driver, description_page_open):
        page = DescriptionPage(driver)
        telegram_url = page.transition_telegram_page()
        assert telegram_url == MainPageLinks.URL_TELEGRAM_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to donate page not authorized user.")
    def test_dp_03_verify_redirection_to_donate_page(self, driver, description_page_open):
        page = DescriptionPage(driver)
        donate_url = page.transition_donate_page()
        assert donate_url == MainPageLinks.URL_DONATE_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to contacts page not authorized user.")
    def test_dp_04_verify_redirection_to_contacts_page(self, driver, main_page_open):
        page = DescriptionPage(driver)
        contacts_page_url = page.transition_contacts_page()
        assert contacts_page_url == MainPageLinks.URL_CONTACTS_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to specialists page not authorized user.")
    def test_dp_05_verify_redirection_to_specialists_page(self, driver, main_page_open):
        page = DescriptionPage(driver)
        specialists_page_url = page.transition_specialists_page()
        assert specialists_page_url == MainPageLinks.URL_SPECIALISTS_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to github not authorized user.")
    def test_dp_06_verify_redirection_to_github(self, driver, main_page_open):
        page = DescriptionPage(driver)
        github_page_url = page.transition_github()
        assert github_page_url == MainPageLinks.URL_GITHUB, "The link leads to an incorrect page."

    @allure.title("Verify redirection to contributors page not authorized user.")
    def test_dp_07_verify_redirection_to_contributors_page(self, driver, main_page_open):
        page = DescriptionPage(driver)
        contributors_page_url = page.transition_contributors_page()
        assert contributors_page_url == MainPageLinks.URL_CONTRIBUTORS_PAGE, "The link leads to an incorrect page."

    @allure.title("Verify redirection to used resources page not authorized user.")
    def test_dp_08_verify_redirection_to_used_resources_page(self, driver, main_page_open):
        page = DescriptionPage(driver)
        resources_page_url = page.transition_used_resources_page()
        assert resources_page_url == MainPageLinks.URL_USED_RESOURCES_PAGE, "The link leads to an incorrect page."
